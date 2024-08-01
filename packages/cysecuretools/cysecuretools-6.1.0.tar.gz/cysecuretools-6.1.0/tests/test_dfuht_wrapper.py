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

from src.execute.programmer.dfuht_wrapper import Dfuht


class TestConnectHelper(unittest.TestCase):
    """Test case for DFU wrapper"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.dfu = Dfuht(None, None)

    def test_read_cmd_series_min(self):
        cmds = self.dfu._read_cmd_series(0x34000000, 1)  # pylint: disable=W0212
        self.assertEqual(0x34000000, cmds[0].addr)
        self.assertEqual(1, cmds[0].size)

    def test_read_cmd_series_256(self):
        cmds = self.dfu._read_cmd_series(0x34000000, 256)  # pylint: disable=W0212
        self.assertEqual(1, len(cmds))
        self.assertEqual(0x34000000, cmds[0].addr)
        self.assertEqual(256, cmds[0].size)

    def test_read_cmd_series_257(self):
        cmds = self.dfu._read_cmd_series(0x34000000, 257)  # pylint: disable=W0212
        self.assertEqual(2, len(cmds))
        self.assertEqual(0x34000000, cmds[0].addr)
        self.assertEqual(256, cmds[0].size)
        self.assertEqual(0x34000100, cmds[1].addr)
        self.assertEqual(1, cmds[1].size)

    def test_read_cmd_series_packet_max(self):
        addr = 0x34000000
        size = 16384
        cmds = self.dfu._read_cmd_series(addr, size)  # pylint: disable=W0212
        for cmd in cmds:
            self.assertEqual(addr, cmd.addr)
            self.assertEqual(256, cmd.size)
            addr += 256
        self.assertEqual(64, len(cmds))

    def test_read_cmd_series_packet_max_and_byte(self):
        addr = 0x34000000
        size = 16385
        cmds = self.dfu._read_cmd_series(addr, size)  # pylint: disable=W0212
        self.assertEqual(65, len(cmds))
        self.assertEqual(addr + size - 1, cmds[64].addr)
        self.assertEqual(1, cmds[64].size)


if __name__ == '__main__':
    unittest.main()
