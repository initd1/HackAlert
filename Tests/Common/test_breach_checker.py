import unittest
from Common.breach_checker import BreachChecker


class BreachChecker(unittest.TestCase):
    def setUp(self):
        self.emails = [
                "test@gmail.com",
                "testgmail.com",
                "test@@gmail",
                "123@gmail.com.au"
                ]

    def test_is_valid_email(self):
        self.assertTrue(self.emails[0])
