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
import json
import os
import unittest

from src.execute.image_signing.sign_tool import SignTool

from tests.utils import keygen


class TestSignTool(unittest.TestCase):
    """Tests common signing images functionality"""

    image = 'image.bin'
    key = 'ecdsa_private_key.pem'
    encrypt_key = 'ecdsa_public_key.pem'
    image_config = 'image_config.json'

    @classmethod
    def setUpClass(cls) -> None:
        with open(cls.image, 'wb') as f:
            f.write(b'AABBCCDD' * 200)
        with open(cls.key, 'w') as f:
            f.write(keygen.ec_private_pem('P-256'))
        with open(cls.encrypt_key, 'w') as f:
            f.write(keygen.ec_public_pem('P-256'))
        with open(cls.image_config, 'w') as f:
            f.write(cls.image_config_data())

    def test_sign_image(self):
        img = SignTool().sign_image(
            self.image,
            key_path=self.key,
            image_config=self.image_config,
            header_size=64,
            slot_size=0x1400,
            security_counter=0x29,
            image_version='11.22.33+4444',
            pad=True,
            confirm=True,
            tlv=(('0x11', 'dummybytes11'), ('0x12', 'dummybytes12')),
            prot_tlv=(('0x13', 'dummybytes13'), ('0x14', 'dummybytes14'))
        )

        with self.subTest('is signed'):
            self.assertTrue(img.is_signed)

        with self.subTest('has ECDSA256 TLV'):
            self.assertEqual(1, len([tlv for tlv in img.tlv if tlv.tag == 0x22]))

        with self.subTest('custom header size'):
            self.assertEqual(64, len(img.header.header_bytes()))

        with self.subTest('custom image version'):
            self.assertEqual(11, img.header.img_version.major)
            self.assertEqual(22, img.header.img_version.minor)
            self.assertEqual(33, img.header.img_version.revision)
            self.assertEqual(4444, img.header.img_version.build)

        with self.subTest('pad to slot size'):
            self.assertEqual(0x1400, img.size)

        with self.subTest('image_ok is 0x01'):
            max_align = 8
            upgrade_img_magic_size = 16
            self.assertEqual(1, img.data[-(upgrade_img_magic_size + max_align)])

        with self.subTest('has custom TLVs'):
            tlv_0x11 = [tlv for tlv in img.tlv if tlv.tag == 0x11]
            tlv_0x12 = [tlv for tlv in img.tlv if tlv.tag == 0x12]
            self.assertEqual(1, len(tlv_0x11))
            self.assertEqual(b'dummybytes11', tlv_0x11[0].value)
            self.assertEqual(1, len(tlv_0x12))
            self.assertEqual(b'dummybytes12', tlv_0x12[0].value)

        with self.subTest('has protected SEC_CNT TLV'):
            tlv_0x50 = [tlv for tlv in img.protected_tlv if tlv.tag == 0x50]
            self.assertEqual(1, len(tlv_0x50))
            self.assertEqual(bytes.fromhex('29000000'), tlv_0x50[0].value)

        with self.subTest('has custom protected TLVs'):
            tlv_0x13 = [tlv for tlv in img.protected_tlv if tlv.tag == 0x13]
            tlv_0x14 = [tlv for tlv in img.protected_tlv if tlv.tag == 0x14]
            self.assertEqual(1, len(tlv_0x13))
            self.assertEqual(b'dummybytes13', tlv_0x13[0].value)
            self.assertEqual(1, len(tlv_0x14))
            self.assertEqual(b'dummybytes14', tlv_0x14[0].value)

        with self.subTest('has image config protected TLVs'):
            tlv_0xf1 = [tlv for tlv in img.protected_tlv if tlv.tag == 0xf1]
            tlv_0xf2 = [tlv for tlv in img.protected_tlv if tlv.tag == 0xf2]
            self.assertEqual(1, len(tlv_0xf1))
            self.assertEqual(bytes.fromhex('00c6002000040000'), tlv_0xf1[0].value)
            self.assertEqual(1, len(tlv_0xf2))
            self.assertEqual(bytes.fromhex('0030002000100000'), tlv_0xf2[0].value)

    def test_sign_image_encrypted(self):
        img = SignTool().sign_image(
            self.image,
            key_path=self.key,
            encrypt=self.encrypt_key
        )

        with self.subTest('is signed'):
            self.assertTrue(img.is_signed)

        with self.subTest('has ECDSA256 TLV'):
            self.assertEqual(1, len([tlv for tlv in img.tlv if tlv.tag == 0x22]))

        with self.subTest('has ENCEC256 TLV'):
            self.assertEqual(1, len([tlv for tlv in img.tlv if tlv.tag == 0x32]))

    def test_sign_image_public_key(self):
        self.assertRaisesRegex(
            ValueError, f'Signing image with public key ',
            SignTool().sign_image, self.image,  key_path=self.encrypt_key)

    def test_add_metadata(self):
        img, decrypted = SignTool().add_metadata(
            self.image,
            image_config=self.image_config,
            header_size=64,
            slot_size=0x1400,
            security_counter=0x29,
            image_version='11.22.33+4444',
            pad=True,
            confirm=True,
            tlv=(('0x11', 'dummybytes11'), ('0x12', 'dummybytes12')),
            prot_tlv=(('0x13', 'dummybytes13'), ('0x14', 'dummybytes14'))
        )

        with self.subTest('is not signed'):
            self.assertFalse(img.is_signed)

        with self.subTest('no decrypted'):
            self.assertIsNone(decrypted)

        with self.subTest('has no ECDSA256 TLV'):
            self.assertEqual(0, len([tlv for tlv in img.tlv if tlv.tag == 0x22]))

        with self.subTest('custom header size'):
            self.assertEqual(64, len(img.header.header_bytes()))

        with self.subTest('custom image version'):
            self.assertEqual(11, img.header.img_version.major)
            self.assertEqual(22, img.header.img_version.minor)
            self.assertEqual(33, img.header.img_version.revision)
            self.assertEqual(4444, img.header.img_version.build)

        with self.subTest('pad to slot size'):
            self.assertEqual(0x1400, img.size)

        with self.subTest('image_ok is 0x01'):
            max_align = 8
            upgrade_img_magic_size = 16
            self.assertEqual(1, img.data[-(upgrade_img_magic_size + max_align)])

        with self.subTest('has custom TLVs'):
            tlv_0x11 = [tlv for tlv in img.tlv if tlv.tag == 0x11]
            tlv_0x12 = [tlv for tlv in img.tlv if tlv.tag == 0x12]
            self.assertEqual(1, len(tlv_0x11))
            self.assertEqual(b'dummybytes11', tlv_0x11[0].value)
            self.assertEqual(1, len(tlv_0x12))
            self.assertEqual(b'dummybytes12', tlv_0x12[0].value)

        with self.subTest('has protected SEC_CNT TLV'):
            tlv_0x50 = [tlv for tlv in img.protected_tlv if tlv.tag == 0x50]
            self.assertEqual(1, len(tlv_0x50))
            self.assertEqual(bytes.fromhex('29000000'), tlv_0x50[0].value)

        with self.subTest('has custom protected TLVs'):
            tlv_0x13 = [tlv for tlv in img.protected_tlv if tlv.tag == 0x13]
            tlv_0x14 = [tlv for tlv in img.protected_tlv if tlv.tag == 0x14]
            self.assertEqual(1, len(tlv_0x13))
            self.assertEqual(b'dummybytes13', tlv_0x13[0].value)
            self.assertEqual(1, len(tlv_0x14))
            self.assertEqual(b'dummybytes14', tlv_0x14[0].value)

        with self.subTest('has image config protected TLVs'):
            tlv_0xf1 = [tlv for tlv in img.protected_tlv if tlv.tag == 0xf1]
            tlv_0xf2 = [tlv for tlv in img.protected_tlv if tlv.tag == 0xf2]
            self.assertEqual(1, len(tlv_0xf1))
            self.assertEqual(bytes.fromhex('00c6002000040000'), tlv_0xf1[0].value)
            self.assertEqual(1, len(tlv_0xf2))
            self.assertEqual(bytes.fromhex('0030002000100000'), tlv_0xf2[0].value)

    def test_add_metadata_encrypted(self):
        img, decrypted = SignTool().add_metadata(
            self.image,
            encrypt=self.encrypt_key
        )

        with self.subTest('is not signed'):
            self.assertFalse(img.is_signed)

        with self.subTest('decrypted'):
            self.assertEqual(b'AABBCCDD' * 200, decrypted.body)

        with self.subTest('has no ECDSA256 TLV'):
            self.assertEqual(0, len([tlv for tlv in img.tlv if tlv.tag == 0x22]))

    def test_add_metadata_encrypted_no_decrypted_arg(self):
        self.assertRaisesRegex(
            ValueError,
            "Arguments 'output' and 'decrypted' must be initialized together",
            SignTool().add_metadata,
            self.image, encrypt=self.encrypt_key, output='output.bin'
        )

    def test_extract_payload(self):
        img, _ = SignTool().add_metadata(self.image)
        payload = SignTool.extract_payload(img.data)
        self.assertEqual(img.payload, payload)

    def test_extract_payload_no_metadata(self):
        self.assertRaisesRegex(ValueError, 'The image does not have metadata',
                               SignTool.extract_payload, b'AABBCCDD' * 200)

    def test_verify_image_verified(self):
        img = SignTool().sign_image(
            self.image,
            key_path=self.key,
        )
        self.assertTrue(SignTool.verify_image(img, self.key))

    def test_verify_image_not_verified(self):
        img = SignTool().sign_image(
            self.image,
            key_path=self.key,
        )
        self.assertFalse(SignTool.verify_image(img, self.encrypt_key))

    def test_verify_image_not_signed(self):
        self.assertRaisesRegex(
            ValueError, 'Image is not signed',
            SignTool.verify_image, self.image, self.key)

    @classmethod
    def tearDownClass(cls) -> None:
        for tmp in (cls.image, cls.key, cls.encrypt_key, cls.image_config):
            os.unlink(tmp)

    @staticmethod
    def image_config_data():
        return json.dumps(
            {
                "tlv": [
                    {
                        "name": "input-params",
                        "tag": "0xF1",
                        "value": [
                            {
                                "name": "address",
                                "value": "0x2000C600",
                                "length": 4
                            },
                            {
                                "name": "size",
                                "value": "0x400",
                                "length": 4
                            }
                        ]
                    },
                    {
                        "name": "output-params",
                        "tag": "0xF2",
                        "value": [
                            {
                                "name": "address",
                                "value": "0x20003000",
                                "length": 4
                            },
                            {
                                "name": "size",
                                "value": "0x1000",
                                "length": 4
                            }
                        ]
                    }
                ]
            }
        )


if __name__ == '__main__':
    unittest.main()
