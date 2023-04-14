import unittest
import sys
import os

sys.path.insert(0, os.getcwd())
from Common.utils import Validator



class TestUtils(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()
        self.ip_addresses = {
            "valid": [
                "192.168.0.1",
                "10.0.0.1",
                "172.16.0.1",
                "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "2001:db8:85a3:0:0:8a2e:370:7334",
                "2001:db8:85a3::8a2e:370:7334",
            ],
            "invalid": [
                "300.168.0.1",
                "10.0.0.256",
                "172.16.0.0/24",
                "2001:0db8:85a3:00000:0000:8a2e:0370:7334",
                "2001:db8:85a3:0:0:8a2e:370:73341",
                "2001:db8:::1:1:1:1:1:1",
            ],
        }


    def tearDown(self):
        del self.validator

    def test_is_valid_ip(self):
        for address in self.ip_addresses["valid"]:
            self.assertTrue(self.validator.is_valid_ip(address))
        for address in self.ip_addresses["invalid"]:
            self.assertFalse(self.validator.is_valid_ip(address))
