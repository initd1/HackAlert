import configparser
import unittest
import sys
import os
sys.path.insert(0, os.getcwd())
from Config import check_config_validity


class TestConfigValid(unittest.TestCase):
    def setUp(self):
        check_config_validity.read_config()
        self.config = configparser.ConfigParser()

    def test_key_value_format(self):
        self.assertIsInstance(self.config.getint('handlers', 'console.level'), int)
        self.assertIsInstance(self.config.getint('loggers', 'keys.suspicious.level'), int)

    def test_keys_present_in_handlers(self):
        assert self.config['loggers'] or 'suspicious' in self.config ['loggers']

    def test_sections_present(self):
        assert 'loggers' in self.config.sections() or 'handlers' in self.config.sections()