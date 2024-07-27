#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SPDX-License-Identifier: GPL-3.0-or-later
Copyright (c) 2023 Savoir-faire Linux

Uses all the builders to complete a full build of a package.
"""

import os
import contextlib
import shutil

from ..utils.logger import log
from ..utils.process import sh_exec
from ..dev_env.vs_env import VSEnv
from .cmake_builder import CMakeBuilder
from .msb_builder import MsbBuilder


@contextlib.contextmanager
def cwd(path):
    owd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(owd)

# Composes the builders to build a package.
class MetaBuilder:
    def __init__(self, base_dir, install_dir=None):
        """
        Use the various builders to build a package based on its info.

        :param base_dir: The base directory where the packages are located.
        :param install_dir: The directory where packages will be installed.
                            If None, the install won't be done.
        """
        self.vs_env = None
        self.cmake_builder = None
        self.msb_builder = None
        self.base_dir = base_dir
        self.vs_env_init_cb = None

        self.install_dir = install_dir # install prefix
        if install_dir is not None:
            self.install_dir = os.path.abspath(install_dir)
            # Make sure the install directory exists
            if not os.path.exists(self.install_dir):
                os.makedirs(self.install_dir)
                # Make bin, lib, and include directories
                os.makedirs(os.path.join(self.install_dir, "bin"))
                os.makedirs(os.path.join(self.install_dir, "lib"))
                os.makedirs(os.path.join(self.install_dir, "include"))

    def set_vs_env_init_cb(self, cb):
        self.vs_env_init_cb = cb

    def initialize_vs_env(self):
        if self.vs_env is not None:
            return

        self.vs_env = VSEnv()
        if not self.vs_env.validated:
            log.error("A valid Visual Studio env is not installed on this machine.")
            return
        self.cmake_builder = CMakeBuilder(self.vs_env)
        self.msb_builder = MsbBuilder(self.vs_env)

        # Call the user's callback to initialize the VS env
        if self.vs_env_init_cb is not None:
            self.vs_env_init_cb()

        # TODO: libjami: replace CMAKE_GENERATOR with use_cmake
        #       found in package info for: fmt, opencv, minizip, yaml-cpp
        sh_exec.append_extra_env_vars({
            "CMAKE_GENERATOR": '"{}"'.format(self.vs_env.cmake_generator),
        })

        # Finally, append the VS env vars
        sh_exec.append_extra_env_vars(self.vs_env.vars)

    def __copy_files_flat(self, src_dir, dst_dir, extensions):
        """
        Copy files with given extensions from source directory to destination directory.
        The folder structure is not preserved (flattened).

        :param src_dir: Source directory from where files are copied.
        :param dst_dir: Destination directory to where files are copied.
        :param extensions: List of file extensions to be copied.
        """
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        for root, dirs, files in os.walk(src_dir):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    src_file_path = os.path.join(root, file)
                    dst_file_path = os.path.join(dst_dir, file)
                    shutil.copy2(src_file_path, dst_file_path)
                    print(f"Copied: {src_file_path} to {dst_file_path}")

    def install(self, pkg):
        """
        Install the package to the install directory.
        This includes copying the headers, libraries, and binaries to the
        appropriate install sub-directories.
        """
        # Assumption: pkg has attributes like 'headers', 'libs', 'binaries'
        # which point to the respective files or directories.
        log.info("Installing " + pkg.name)

        if self.install_dir is None:
            log.error(f"No install directory specified for {pkg.name}")
            return False

        try:
            scan_dir = pkg.buildsrc_dir

            # Includes
            dst = os.path.join(self.install_dir, "include")
            for root, dirs, _ in os.walk(scan_dir):
                if "include" in dirs:
                    src = os.path.join(root, "include")
                    log.debug(f"Copying headers in {src} to {dst}")
                    os.makedirs(dst, exist_ok=True)
                    os.system(f"xcopy /Y /E /I {src}\*.h {dst} >nul 2>&1")
                    os.system(f"xcopy /Y /E /I {src}\*.hpp {dst} >nul 2>&1")

            # Libraries
            dst = os.path.join(self.install_dir, "lib")
            self.__copy_files_flat(scan_dir, dst, [".lib"])

            # Binaries
            dst = os.path.join(self.install_dir, "bin")
            self.__copy_files_flat(scan_dir, dst, [".dll", ".exe"])

        except Exception as e:
            log.warning(f"Problem installing {pkg.name}: {e}")
            return False


    def build(self, pkg):
        log.info("Building " + pkg.name)

        try:
            target_dir = os.getcwd()
            if os.path.exists(pkg.buildsrc_dir):
                target_dir = pkg.buildsrc_dir
            with cwd(target_dir):
                self.initialize_vs_env()

                # If we can use CMake, we should configure with it here.
                if pkg.use_cmake:
                    # Configure with CMake
                    log.debug(f"CMake configure for {pkg.name}")
                    if not self.cmake_builder.configure(pkg):
                        raise Exception("Error configuring with CMake")

                # pre_build custom step (custom CMake...)
                pre_build_scripts = pkg.custom_scripts.get("pre_build", [])
                if pre_build_scripts:
                    log.debug(f"Pre-Build for {pkg.name}")
                    for script in pre_build_scripts:
                        res = sh_exec.cmd(script)
                        if res[0] != 0:
                            raise Exception("Error executing pre-build script")

                # build with CMake
                if pkg.use_cmake:
                    # Build with CMake
                    log.debug(f"CMake build for {pkg.name}")
                    if not self.cmake_builder.build(pkg):
                        raise Exception("Error building with CMake")

                # build custom step (nmake...)
                build_scripts = pkg.custom_scripts.get("build", [])
                if build_scripts:
                    log.debug(f"Custom build for {pkg.name}")
                    for script in build_scripts:
                        res = sh_exec.cmd(script)
                        if res[0] != 0:
                            raise Exception("Error executing custom build script")

                # vcxproj files
                if pkg.project_paths:
                    log.debug(f"Msbuild phase for {pkg.name}")
                    for pp in pkg.project_paths:
                        project_full_path = os.path.join(pkg.buildsrc_dir, pp)
                        if not self.msb_builder.build(
                            pkg.name,
                            project_full_path,
                            self.vs_env.sdk_version,
                            self.vs_env.toolset_default,
                            pkg.with_env,
                        ):
                            raise Exception("Error building with MSBuild")

                post_build_scripts = pkg.custom_scripts.get("post_build", [])
                if post_build_scripts:
                    log.debug(f"Post-Build for {pkg.name}")
                    for script in post_build_scripts:
                        result = sh_exec.cmd(script)
                        if result[0] != 0:
                            raise Exception("Error executing post-build script")

                log.debug(f"Build complete for {pkg.name}")
                # Maybe install the package?
                if self.install_dir is not None:
                    self.install(pkg)
        except Exception as e:
            log.error(f"Error building {pkg.name}: {e}")
            return False

        return True
