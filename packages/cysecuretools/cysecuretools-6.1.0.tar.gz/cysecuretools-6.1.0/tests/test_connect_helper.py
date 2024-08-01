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
import unittest
from unittest.mock import MagicMock, patch

from src.core.connect_helper import ConnectHelper
from src.core.logging_configurator import LoggingConfigurator
from src.execute.programmer.openocd_wrapper import Openocd


class TestConnectHelper(unittest.TestCase):
    """Test case for ConnectHelper"""

    @classmethod
    def setUpClass(cls) -> None:
        LoggingConfigurator.disable_logging()

    @patch('os.path.exists')
    @patch('src.core.connect_helper.ConnectHelper.discover_tool')
    def test_connect_mtb_ocd_path(self, discover_tool_mock, path_exists_mock):
        openocd = Openocd('openocd', None)
        target_mock = MagicMock()
        setattr(target_mock, 'ocds', ['openocd'])
        discover_tool_mock.return_value = 'dummy_path'
        path_exists_mock.return_value = True
        ConnectHelper.connected = True
        ConnectHelper.connect(openocd, target_mock)
        self.assertEqual('dummy_path', openocd.tool_path)

    @patch('os.path.exists')
    @patch('src.core.connect_helper.ConnectHelper.discover_tool')
    def test_connect_existing_path(self, discover_tool_mock, path_exists_mock):
        ocd_settings_mock = MagicMock()
        setattr(ocd_settings_mock, 'ocd_name', 'openocd')
        setattr(ocd_settings_mock, 'ocd_path', 'dummy_path')
        openocd = Openocd('openocd', ocd_settings_mock)
        target_mock = MagicMock()
        setattr(target_mock, 'ocds', ['openocd'])
        discover_tool_mock.return_value = 'dummy_path'
        path_exists_mock.return_value = True
        ConnectHelper.connected = True
        ConnectHelper.connect(openocd, target_mock)
        self.assertEqual('dummy_path', openocd.tool_path)

    @patch('src.core.connect_helper.mtb_openocd_dir')
    def test_discover_tool(self, mtb_openocd_dir_mock):
        mtb_openocd_dir_mock.return_value = 'dummy_path'
        self.assertEqual('dummy_path', ConnectHelper.discover_tool('openocd'))

    @classmethod
    def tearDownClass(cls) -> None:
        LoggingConfigurator.enable_logging()


if __name__ == '__main__':
    unittest.main()
