#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SPDX-License-Identifier: GPL-3.0-or-later
Copyright (c) 2023 Savoir-faire Linux

Used to configure/build with CMake.
"""

import os
from ..utils.logger import log
from ..utils.process import sh_exec


class CMakeBuilder:
    def __init__(self, vs_env) -> None:
        self.vs_env = vs_env

    def build(self, pkg):
        log.info("Building " + pkg.name + " with CMake")
        args = [
            '--build', os.path.join(pkg.buildsrc_dir, 'build'),
            '--config', 'Release',
            '--target', 'ALL_BUILD'
        ]
        result = sh_exec.cmd('cmake', args)
        if not result[0]:
            return True
        return False

    def configure(self, pkg):
        log.info("Configuring with Cmake")
        args = [
            '-G', self.vs_env.cmake_generator,
            '-A', self.vs_env.arch,
            '-S', pkg.buildsrc_dir,
            '-B', os.path.join(pkg.buildsrc_dir, 'build')
        ]
        args.extend(['-D' + define for define in pkg.defines])
        result = sh_exec.cmd('cmake', args)
        if not result[0]:
            return True
        log.error("Error configuring with CMake")
        return False
