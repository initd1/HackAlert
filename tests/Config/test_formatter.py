import os
import sys
import unittest
import logging
sys.path.insert(0, os.getcwd())
from Config.formatter import Formatter
from Config.config import configure_logging


class TestFormatter(unittest.TestCase):
    def setUp(self):
        # Ensure file paths are all set up
        if not os.path.split(os.path.basename(os.getcwd()))[1] == "HackAlert":
            print("Pathname invalid, ensure you're in the base directory.")
            sys.exit(1)
        if not os.path.isdir(os.path.join("logs")) or not os.path.isdir(os.path.join("logs", "tests")):
            os.makedirs(os.path.join('logs', 'tests'))
            files = [os.path.join("logs/tests/test_critical.log"),
                     os.path.join("logs/tests/test_error.log"),
                     os.path.join("logs/tests/test_warning.log"),
                     os.path.join("logs/tests/test_debug.log"),
                     os.path.join("logs/tests/test_info.log")]
            for file_ in files:
                if not os.path.exists(file_):
                    with open(file_, "w") as file:
                        file.write(f"Created {file_} for tests.")
                        file.close()

        configure_logging()
        self.formatter = Formatter()
        self.logger = logging.getLogger()

    def test_records(self):
        self.records = {
                "critical": self.logger.makeRecord( "test_critical", logging.CRITICAL, "logs/tests/test_critical.log", 50, "[test] critical message", (), None,),
                "error": self.logger.makeRecord( "test_error", logging.ERROR, "logs/tests/test_error.log", 40, "[test] error message", (), None,),
                "warning": self.logger.makeRecord( "test_warning", logging.WARNING, "logs/tests/test_warning.log", 30, "[test] warning message", (), None,),
                "debug": self.logger.makeRecord( "test_debug", logging.DEBUG, "logs/tests/test_debug.log", 20, "[test] debug message", (), None,),
                "info": self.logger.makeRecord( "test_info", logging.INFO, "logs/tests/test_info.log", 10, "[test] info message", (), None,),
                }

        for record in self.records.keys():
            if self.assertIsInstance(self.records[record], logging.LogRecord) is not False:
                self.assertIn(record, self.records[record].msg)

