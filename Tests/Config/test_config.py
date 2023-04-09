import os
import unittest
from configparser import ConfigParser

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join('Config/logger.ini')

        if not os.path.exists(os.path.join('Logs', 'traceback.log')):
            with open(os.path.join('Logs', 'traceback.log')) as fp:
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
        

if __name__ == "__main__":
    unittest.main()
