"""
Copyright 2022-2024 Cypress Semiconductor Corporation (an Infineon company)
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

from src.core import bitops


class TestBitOps(unittest.TestCase):
    """Tests for a module containing general functions for
    bitwise and bytewise operations"""

    def test_number_size_1_zero(self):
        self.assertEqual(bitops.number_size(0x00), 1)

    def test_number_size_1(self):
        self.assertEqual(bitops.number_size(0x11), 1)

    def test_number_size_2(self):
        self.assertEqual(bitops.number_size(0x1122), 2)

    def test_number_size_3(self):
        self.assertEqual(bitops.number_size(0x112233), 3)

    def test_number_size_4(self):
        self.assertEqual(bitops.number_size(0x11223344), 4)

    def test_number_size_27(self):
        self.assertEqual(bitops.number_size(
            0x00000033445566778899AABBCCDDEEFF00112233445566778899AABBCCDD), 27)


if __name__ == '__main__':
    unittest.main()
