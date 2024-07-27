#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SPDX-License-Identifier: GPL-3.0-or-later
Copyright (c) 2023 Savoir-faire Linux

VLC-style contrib package versioning and build information management.
Used to fetch, patch, and build packages with an understanding of their
dependencies.
"""

import os
import sys

from ..utils.logger import log
from ..utils.process import sh_exec
from .package import Package, PKG_FILE_NAME
from .fetcher import Fetcher
from .patcher import Patcher
from ..builders.meta_builder import MetaBuilder
from .build_tools import Operation


class Versioner:
    def __init__(self, base_dir, install_dir=None):
        self.pkgs = {}
        self.base_dir = base_dir
        self.install_dir = install_dir
        # Check base_dir and verify that its structure is valid.
        if not os.path.exists(self.base_dir):
            raise RuntimeError(f"Base directory does not exist {self.base_dir}")

        self.src_dir = os.path.join(self.base_dir, "src")
        self.buildsrc_dir = os.path.join(self.base_dir, "build")
        self.fetch_dir = os.path.join(self.base_dir, "tarballs")

        self.fetcher = Fetcher(self.fetch_dir, self.buildsrc_dir)
        self.patcher = Patcher(self.src_dir, self.buildsrc_dir)

        self.builder = MetaBuilder(base_dir=self.base_dir,
                                   install_dir=self.install_dir)

        # Allow to exclude some packages from the build.
        self.exclusion_list = []

        # Alternate build output directories.
        self.extra_output_dirs = []

        # List of up-to-date packages (for this session) used to avoid
        # rechecking dependency package chains that have already been brought
        # up-to-date this session.
        self.uptodate_pkgs = []

    @staticmethod
    def print_info(pkg):
        # Debug with short hashes (6 chars) for the build version, and md5.
        build_version = pkg.build_version[:6] if pkg.build_version else None
        # Truncate the version to 6 chars if it's a git hash.
        version = pkg.version[:7] if len(pkg.version) == 40 else pkg.version
        md5 = pkg.src_md5[:7] if pkg.src_md5 else None
        log.info(f"Package {pkg.name} (req-ver: {version}"
                 f" - build:{build_version}:source:{md5})")

    # Load a package's versioning information from its JSON file, and
    # analyze it to determine the package's version and build information,
    # as well as its dependencies.
    def load_package(self, pkg_name):
        # Check if it's already been loaded.
        if pkg_name in self.pkgs:
            return self.pkgs[pkg_name]

        log.debug(f"Loading package info for {pkg_name}")

        # Build an object from the package's versioning information from its JSON file.
        pkg = Package(pkg_name, self.src_dir, self.buildsrc_dir)
        if pkg.info is None:
            raise RuntimeError(f"Could not load package info for {pkg_name}")

        # Add the package to the list of packages.
        self.pkgs[pkg_name] = pkg

        # Return the package.
        return pkg

    # Check if the package's build directory is up-to-date with respect to
    # the package's source directory. Used to trigger rebuilds when the
    # source build directory has been modified.
    def is_build_uptodate(self, pkg):
        if not os.path.exists(pkg.build_version_file):
            return False
        file_list = []
        for path, _, files in os.walk(pkg.buildsrc_dir):
            for name in files:
                file_list.append(os.path.join(path, name))
        if not file_list:
            return False
        latest_file = max(file_list, key=os.path.getmtime)
        t_mod = os.path.getmtime(latest_file)
        t_build = os.path.getmtime(pkg.build_version_file)
        return t_mod < t_build

    def exec_for_all(self, op, force=False):
        """
        Fetch/patch/build all packages in the src directory that contain
        package.json files. Returns on first failure.
        """
        pkgs = os.listdir(self.src_dir)
        # Filter out non-package directories, and directories that are in the
        # exclusion list.
        pkgs = [
            pkg
            for pkg in pkgs
            if os.path.exists(os.path.join(self.src_dir, pkg, PKG_FILE_NAME))
            and pkg not in self.exclusion_list
        ]
        # Print the list of packages to be built.
        log.info(f"Building packages: {pkgs}")
        for pkg in pkgs:
            if not self.exec_for_pkg(pkg, op, force=force, recurse=True):
                log.error(f"Failed to build {pkg}")
                return False
        return True

    def exec_for_pkg(self, pkg_name, op, parent_pkg=None, force=False, recurse=False):
        """
        Fetch/patch/build a package and its dependencies.
        """
        # NOTE: this function is recursive, and tail recursive.
        # Load the package's versioning information.

        if pkg_name in self.uptodate_pkgs:
            return True

        op_str = op.__str__().lower()
        log.info(f"Doing {op_str} for {pkg_name}")

        try:
            pkg = self.load_package(pkg_name)
        except RuntimeError as e:
            log.error(f"{e}")
            return False

        result = self.make(pkg, op, parent_pkg, force, recurse)
        if not result:
            log.error(f"Failed to {op_str} {pkg_name}")
        else:
            log.info(f"{op_str} complete for {pkg_name}")
            self.uptodate_pkgs.append(pkg_name)
        return result

    def make(self, pkg, op, parent_pkg=None, force=False, recurse=False):
        # Print the package's info.
        self.print_info(pkg)

        # Check if the package is already up-to-date.
        pkg.build_uptodate = self.is_build_uptodate(pkg)

        # Now check the package's dependencies.
        if recurse and op not in [Operation.CLEAN]:
            for dep in pkg.deps:
                log.debug(f"Checking {pkg.name} dependency {dep}")
                #----------------------------------------------------------
                # !!!!! RECURSION !!!!! exec_for_pkg->make->exec_for_pkg...
                #----------------------------------------------------------
                if not self.exec_for_pkg(dep, parent_pkg=pkg, op=op, recurse=True):
                    log.debug(f"Failed to build dependency {dep}")
                    return False

        # If the package's source code dir and build timestamp are already
        # up-to-date, and we're not forcing a rebuild, then we're done.
        if pkg.build_uptodate and pkg.ver_uptodate and not force:
            log.info(f"Package {pkg.name} is already up-to-date.")
            return True
        elif pkg.build_version is not None:
            if not pkg.build_uptodate:
                log.info(f"Source code for {pkg.name} has changed.")
            if not pkg.ver_uptodate:
                log.info(f"Rules for {pkg.name} have changed.")

        # If we're building a dependency, we want to force a rebuild of the
        # parent package, so that it will be rebuilt with the new dependency.
        if parent_pkg is not None:
            # Remove the parent package from the list of up-to-date packages.
            if parent_pkg.name in self.uptodate_pkgs:
                self.uptodate_pkgs.remove(parent_pkg.name)
            # Mark the parent package as not up-to-date and remove its build version.
            parent_pkg.build_uptodate = False
            parent_pkg.build_version = None
            # In case the script is terminated, we want to save the parent package's
            # dirty state to disk, so delete the parent package's build version file.
            if os.path.exists(parent_pkg.build_version_file):
                os.remove(parent_pkg.build_version_file)

        # FETCH, RESOLVE
        if op in [Operation.FETCH, Operation.RESOLVE]:
            # First fetch the package if it's not already fetched.
            if not pkg.src_uptodate or force:
                reason = "(forced)" if force else "out-of-date"
                log.info(f"Cleaning {reason} {pkg.name}")
                # Clean the package's build source directory.
                if os.path.exists(pkg.buildsrc_dir):
                    self.fetcher.clean_pkg(pkg)

            if not os.path.exists(pkg.buildsrc_dir) or force:
                if not self.fetcher.fetch_pkg(pkg, force):
                    log.error(f"Failed to fetch {pkg.name}")
                    return False

            # Track the source fetch.
            pkg.track_src_fetch()

        # PATCH, RESOLVE
        if op in [Operation.PATCH, Operation.RESOLVE]:
            if not pkg.is_patched or force:
                # Apply patches if the package has any.
                if not self.patcher.apply_all(pkg):
                    # This is a special case, we don't want to fail the build
                    # if a patch fails to apply, we just want to warn the user
                    # of what happened, print some likely reasons, and continue.
                    log.error(f"Failed to apply patches for {pkg.name}"
                            " (Patches may be either aleady applied,"
                            " or the source code has changed.)")
                    return False

                # Now we need to track the patched state.
                pkg.track_src_patch()

        # BUILD, RESOLVE
        if op in [Operation.BUILD, Operation.RESOLVE]:
            # Actually build the package.
            if not pkg.build_uptodate or not pkg.ver_uptodate or force:
                if not self.builder.build(pkg):
                    log.error(f"Failed to build {pkg.name}")
                    return False

            # Finally, update the package's up-to-date state.
            # Track the source fetch.
            pkg.track_src_build()
            pkg.ver_uptodate = True
            log.debug(f"Package {pkg.name} is now up-to-date.")

        return True

    def clean_all(self):
        return self.clean_tarballs() and self.clean_builds()

    def clean_tarballs(self):
        return self.fetcher.clean_tarballs()

    def clean_pkg_tarball(self, pkg_name):
        try:
            pkg = self.load_package(pkg_name)
        except RuntimeError as e:
            log.error(f"{e}")
            return False
        return self.fetcher.clean_pkg_tarball(pkg)

    def clean_pkg_build(self, pkg_name):
        try:
            pkg = self.load_package(pkg_name)
        except RuntimeError as e:
            log.error(f"{e}")
            return False
        return self.fetcher.clean_pkg_build(pkg)

    def clean_pkg(self, pkg_name):
        try:
            pkg = self.load_package(pkg_name)
        except RuntimeError as e:
            log.error(f"{e}")
            return False
        return self.fetcher.clean_pkg(pkg)

    def clean_install_dir(self):
        if self.install_dir is not None:
            log.info(f"Removing install directory {self.install_dir}")
            ret = sh_exec.cmd("rmdir", ["/s", "/q", self.install_dir])
            if ret[0]:
                log.warn("Failed to clean install directory")

    def clean_builds(self):
        self.clean_install_dir()
        clean_builds = self.fetcher.clean_builds()
        # Clean extra output directories.
        clean_exra_output_dirs = True
        for extra_output_dir in self.extra_output_dirs:
            abs_extra_output_dir = os.path.join(self.base_dir, extra_output_dir)
            if os.path.exists(abs_extra_output_dir):
                log.info(f"Removing extra output directory {abs_extra_output_dir}")
                ret = sh_exec.cmd("rmdir", ["/s", "/q", abs_extra_output_dir])
                if ret[0]:
                    log.error("Failed to clean extra output directory")
                    clean_exra_output_dirs = False
        return clean_builds and clean_exra_output_dirs