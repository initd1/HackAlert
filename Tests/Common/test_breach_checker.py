from re import Match
import unittest
import sys
import os

# NOTE without this, pytest does not recognize tests
sys.path.insert(0, os.getcwd())

# NOTE pyright ignore to prevent Lsp from messing up.
from Common.breach_checker import BreachChecker  # pyright: ignore


class TestBreachChecker(unittest.TestCase):
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

    def test_is_valid_email(self):
        """Recursively checks validity of arrays in `self.emails`"""

        print("\ntest_is_valid_email")
        for state in self.emails:
            for _, email in enumerate(self.emails[state]):
                match state:
                    case "valid":
                        print(email, state)
                        self.assertTrue(BreachChecker.is_valid_email(email))
                    case "invalid":
                        print(email, state)
                        self.assertFalse(BreachChecker.is_valid_email(email))
