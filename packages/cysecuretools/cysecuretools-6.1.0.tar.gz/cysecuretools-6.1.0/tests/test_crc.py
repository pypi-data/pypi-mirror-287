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

from src.core.crc import crc32d6a


class TestCRC(unittest.TestCase):
    """Test case for CRC calculation"""

    def test_crc32d6a(self):
        with self.subTest('Data 1'):
            data = bytearray.fromhex(
                'aa1a40000000f51a40000003f51a40000004f41a4000000118321a4000000'
                '2141a400000051a080060001a400000061a000100001a400000071a101000'
                '001a400000081a000ffe001a400000091a10100000')
            self.assertEqual(0x40a836a7, crc32d6a(data, 0x100D0000))

        with self.subTest('Data 2'):
            data = bytearray.fromhex(
                'aa1a40000000f51a40000003f51a40000004f51a4000000118321a4000000'
                '2141a400000051a080060001a400000061a000100001a400000071a101000'
                '001a400000081a000ffe001a400000091a10100000')
            self.assertEqual(0xa9469412, crc32d6a(data, 0x100D0000))


if __name__ == '__main__':
    unittest.main()
