"""
Copyright 2023-2024 Cypress Semiconductor Corporation (an Infineon company)
or an affiliate of Cypress Semiconductor Corporation. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import unittest
from unittest.mock import patch

from src.core.mtb_tools_discovery import (
    mtb_dir, mtb_tools_dir, mtb_version, mtb_tools, mtb_openocd_dir
)


class TestMTBToolsDiscovery(unittest.TestCase):
    """Test case for ModusToolbox discovery module"""

    @patch('platform.system')
    @patch('os.path.isdir')
    def test_mtb_dir_windows(self, isdir_mock, system_mock):
        system_mock.return_value = 'Windows'
        isdir_mock.return_value = True
        self.assertEqual(os.path.join(os.path.expanduser('~'), 'ModusToolbox'),
                         mtb_dir())

    @patch('platform.system')
    @patch('os.path.isdir')
    def test_mtb_dir_linux(self, isdir_mock, system_mock):
        system_mock.return_value = 'Linux'
        isdir_mock.return_value = True
        self.assertEqual(os.path.join(os.path.expanduser('~'), 'ModusToolbox'),
                         mtb_dir())

    @patch('platform.system')
    @patch('os.path.isdir')
    def test_mtb_dir_macos(self, isdir_mock, system_mock):
        system_mock.return_value = 'Darwin'
        isdir_mock.return_value = True
        self.assertEqual(os.path.join('/', 'Applications', 'ModusToolbox'),
                         mtb_dir())

    @patch('platform.system')
    @patch('os.path.expanduser')
    def test_mtb_dir_macos_path_not_exist(self, expanduser_mock, system_mock):
        system_mock.return_value = 'Linux'
        expanduser_mock.return_value = 'NonExistingHomeDir'
        self.assertIsNone(mtb_dir())

    @patch('os.listdir')
    @patch('src.core.mtb_tools_discovery.mtb_dir')
    def test_mtb_tools_dir(self, mtb_dir_mock, listdir_mock):
        mtb_dir_mock.return_value = 'ModusToolbox'
        listdir_mock.return_value = ['tools_3.0', 'tools_3.1', 't', 'tools_2.4']
        self.assertEqual(os.path.join('ModusToolbox', 'tools_3.1'),
                         mtb_tools_dir())

    @patch('os.environ.get')
    def test_mtb_tools_dir_cy_tools_path(self, environ_mock):
        environ_mock.return_value = 'CustomModusToolboxDir'
        self.assertEqual('CustomModusToolboxDir', mtb_tools_dir())

    @patch('src.core.mtb_tools_discovery.mtb_dir')
    def test_mtb_tools_dir_not_exist(self, mtb_dir_mock):
        mtb_dir_mock.return_value = None
        self.assertIsNone(mtb_tools_dir())

    @patch('os.listdir')
    @patch('src.core.mtb_tools_discovery.mtb_dir')
    def test_mtb_tools_dir_not_found(self, mtb_dir_mock, listdir_mock):
        mtb_dir_mock.return_value = 'ModusToolbox'
        listdir_mock.return_value = []
        self.assertRaisesRegex(
            FileNotFoundError,
            "'tools_X.Y' directory not found in 'ModusToolbox'",
            mtb_tools_dir
        )

    @patch('src.core.mtb_tools_discovery.mtb_tools_dir')
    def test_mtb_version(self, mtb_tools_dir_mock):
        mtb_tools_dir_mock.return_value = os.path.join(
            os.path.expanduser('~'), 'tools_3.1')
        self.assertEqual('3.1', mtb_version())

    @patch('src.core.mtb_tools_discovery.mtb_tools_dir')
    def test_mtb_version_no_mtb(self, mtb_tools_dir_mock):
        mtb_tools_dir_mock.return_value = None
        self.assertIsNone(mtb_version())

    @patch('subprocess.check_output')
    @patch('src.core.mtb_tools_discovery.mtb_tools_dir')
    def test_mtb_tools(self, mtb_tools_dir_mock, check_output_mock):
        check_output_mock.return_value = b'CY_TOOL1=path1\nCY_TOOL2=path2\n'
        mtb_tools_dir_mock.return_value = 'dummy_mtb_tools_path'
        self.assertEqual({'CY_TOOL1': 'path1', 'CY_TOOL2': 'path2'}, mtb_tools())

    @patch('src.core.mtb_tools_discovery.mtb_tools_dir')
    def test_mtb_tools_no_mtb(self, mtb_tools_dir_mock):
        mtb_tools_dir_mock.return_value = 'somenonexistingpath'
        self.assertIsNone(mtb_tools())

    @patch('src.core.mtb_tools_discovery.mtb_tools')
    @patch('src.core.mtb_tools_discovery.mtb_version')
    def test_mtb_openocd_dir_greater_or_equal_3_1(self, mtb_version_mock, mtb_tools_mock):
        mtb_version_mock.return_value = '3.1'
        mtb_tools_mock.return_value = {
            'CY_TOOL_openocd_BASE': 'openocd',
            'CY_TOOL_openocd_BASE_ABS': 'path1',
            'CY_TOOL_openocd_EXE': 'path2',
            'CY_TOOL_openocd_EXE_ABS': 'path3'
        }
        self.assertEqual('path1', mtb_openocd_dir())

    @patch('src.core.mtb_tools_discovery.mtb_tools')
    @patch('src.core.mtb_tools_discovery.mtb_version')
    def test_mtb_openocd_dir_less_than_3_0(self, mtb_version_mock, mtb_tools_mock):
        mtb_tools_mock.return_value = {
            'CY_TOOL_openocd_BASE': 'path1',
            'CY_TOOL_openocd_EXE': 'path2'
        }
        for version in ('2.3', '2.4'):
            with self.subTest(version):
                mtb_version_mock.return_value = version
                self.assertEqual('path1', mtb_openocd_dir())

    @patch('src.core.mtb_tools_discovery.mtb_tools')
    @patch('src.core.mtb_tools_discovery.mtb_version')
    def test_mtb_openocd_dir_no_mtb(self, mtb_version_mock, mtb_tools_mock):
        mtb_tools_mock.return_value = None
        mtb_version_mock.return_value = None
        self.assertIsNone(mtb_openocd_dir())


if __name__ == '__main__':
    unittest.main()
