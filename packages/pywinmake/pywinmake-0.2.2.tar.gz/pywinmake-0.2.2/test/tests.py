#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SPDX-License-Identifier: GPL-3.0-or-later
Copyright (c) 2023 Savoir-faire Linux

Run some actual tests on the pywinmake package, using the test/winmake.py script.
"""

import subprocess
import unittest
import os

class PyWinMakeTests(unittest.TestCase):
    """
    Use Nettle here as a test package because it has 1 dependency (GMP) and is
    small enough to build quickly.
    """

    args = ['-l5', '-v2', '-o', 'install']
    this_dir = os.path.dirname(os.path.realpath(__file__))
    base_command = ['python', os.path.join(this_dir, 'winmake.py')]
    base_command.extend(args)
    subprocess.run(base_command + ['clean'])

    def test_0_resolve_package(self):
        """pjproject has several dependencies, so it's a good test package"""
        result = subprocess.run(self.base_command + ['resolve', 'pjproject', '-f'],
                                stdout=subprocess.PIPE)
        self.assertEqual(result.returncode, 0)
        # Make sure there is at least 1 *.lib file in the lib directory
        # Up one directory, then into the install/lib directory
        lib_dir = os.path.join(os.path.dirname(self.this_dir), 'install', 'lib')
        self.assertGreater(len(os.listdir(lib_dir)), 0)

    def test_1_resolve_package_with_different_name(self):
        """msgpack-c has a different package name than the directory name"""
        result = subprocess.run(self.base_command + ['resolve', 'msgpack', '-f'],
                                stdout=subprocess.PIPE)
        self.assertEqual(result.returncode, 0)
        # Make sure that msgpack.hpp is in the include directory
        # Up one directory, then into the install/include directory
        include_dir = os.path.join(os.path.dirname(self.this_dir), 'install', 'include')
        self.assertIn('msgpack.hpp', os.listdir(include_dir))

    def test_2_build_portaudio_with_missing_state(self):
        """Here we mess with the state file to see we can avoid applying patches multiple times"""
        result = subprocess.run(self.base_command + ['resolve', 'portaudio'],
                                stdout=subprocess.PIPE)
        self.assertEqual(result.returncode, 0)
        # Delete the build target file so we can force a rebuild
        build_dir = os.path.join(os.path.dirname(self.this_dir), 'test', 'contrib', 'build')
        target_file = os.path.join(build_dir, '.portaudio.build')
        self.assertTrue(os.path.exists(target_file))
        os.remove(target_file)
        # Build it again
        result = subprocess.run(self.base_command + ['resolve', 'portaudio'],
                                stdout=subprocess.PIPE)
        self.assertEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()