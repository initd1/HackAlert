import os
import unittest
from configparser import ConfigParser


class TestConfig(unittest.TestCase):
    def setUp(self):
        """Setup is the first method run in the test."""
        self.path = os.path.join("Config/logger.ini")

        if not os.path.isdir("Logs"):
            os.mkdir("Logs")
        if not os.path.exists(os.path.join("Logs", "traceback.log")):
            with open(os.path.join("Logs", "traceback.log"), "w") as fp:
                fp.write("Created traceback.log as part of tests.\n")
                fp.close()

    def test_config_exists(self):
        self.assertTrue(self.path)

    def test_config_is_valid(self):
        parser = ConfigParser()
        if self.test_config_exists:
            parser.read(self.path, encoding='utf-8')
        # Check if the required sections are present in the config
        self.assertIn("formatters", parser.sections())
        self.assertIn("handler_console", parser.sections())

        # Check if the required keys are present in the sections
        self.assertIn("keys", parser["formatters"])
        self.assertIn("level", parser["handler_console"])


if __name__ == "__main__":
    unittest.main()
