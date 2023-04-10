import os
import unittest

import sys

sys.path.insert(0, os.getcwd())

from requests.api import get
from Config.config import configure_logging, get_config, get_logging_config
from configparser import ConfigParser

class TestConfig(unittest.TestCase):
    def setUp(self):
        """ Setup is the first method run in the test."""
        self.path = os.path.join('Config/logger.ini')

        if not os.path.isdir('Logs'):
            os.mkdir('Logs')
        if not os.path.exists(os.path.join('Logs', 'traceback.log')):
            with open(os.path.join('Logs', 'traceback.log'), 'w') as fp:
                fp.write("Created traceback.log as part of tests.")
                fp.close()

    def test_config_exists(self):
        self.assertTrue(self.path)

    def test_config_is_valid(self):
        parser = ConfigParser()
        if self.test_config_exists:
            parser.read(self.path)
        
        # Check if the required sections are present in the config
        self.assertIn('formatters', parser.sections())
        self.assertIn('handler_console', parser.sections())
        
        # Check if the required keys are present in the sections
        self.assertIn('keys', parser['formatters'])
        self.assertIn('level', parser['handler_console'])
        
    def test_directory_structure(self):
        """ Check that config module is where it's supposed to be """ 

        self.assertTrue(os.path.exists(os.path.join("Config", "config.py")))

    def test_get_config(self):
        self.assertIn("property", get_logging_config.__builtins__.keys())

    def test_get_logging_config(self):
        with self.assertRaises(FileNotFoundError) as _:
            get_logging_config("random_path.txt")
        self.assertIsInstance(get_logging_config(), ConfigParser)

    def test_configure_logging(self):
        self.assertIsInstance(configure_logging(), ConfigParser)

if __name__ == "__main__":
    unittest.main()
