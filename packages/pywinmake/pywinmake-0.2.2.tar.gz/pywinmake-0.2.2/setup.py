#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SPDX-License-Identifier: GPL-3.0-or-later
Copyright (c) 2023 Savoir-faire Linux
"""

from setuptools import setup, find_packages

setup(
    name="pywinmake",
    description="A python tool to build Windows packages",
    long_description="This tool is designed to provide a way to build Windows packages in a similar way to the VLC contrib system. By providing a package.json file, you can define the package's version, dependencies, and build rules.",
    version="0.2.2",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "coloredlogs",
    ],
)