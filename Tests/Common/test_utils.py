import unittest
import sys
import os

# NOTE without this, pytest does not recognize tests
sys.path.insert(0, os.getcwd())

# NOTE pyright ignore to prevent Lsp from messing up.
from Common.validator import is_valid_ip, is_valid_email, is_valid_username


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.emails = {
            "valid": [
                "inform2atul@gmail.com",
                "test@gmail.com",
                "person123@hotmail.com",
            ],
            "invalid": [
                "testPerson@wahroonga.adventist.edu.au",
                "student.23@students.mq.edu.au",
                "testgmail.com",
                "test@@gmail",
                "123@gmail.com.au",
            ],
        }

        # TODO add additional edge cases
        self.user_names = {
                "valid": [
                    "test123"
                    "_test_"
                    ],
                "invalid": [
                    "😀",
                    ],
                }

    def test_is_valid_email(self):
        """Recursively checks validity of arrays in `self.emails`"""

        for state in self.emails:
            for email in self.emails[state]:
                match state:
                    case "valid":
                        self.assertTrue(is_valid_email(email))
                    case "invalid":
                        self.assertFalse(is_valid_email(email))

    def test_is_valid_name(self):
        """ Recursively checks the validity of usernames """

        for state in self.user_names:
            for name in self.user_names[state]:
                match state:
                    case "valid":
                        self.assertTrue(is_valid_username(name))
                    case "invalid":
                        self.assertFalse(is_valid_username(name))
