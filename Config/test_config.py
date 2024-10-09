import unittest
from unittest.mock import patch, mock_open, MagicMock
import configparser
import os
import logging
from your_module import get_config, get_logging_config, configure_logging # type: ignore

class TestConfigModule(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="[ENVIRONMENT]\nVAR1=value1")
    @patch("configparser.ConfigParser.read")
    def test_get_config_file_parsed(self, mock_read, mock_open):
        """
        Test if the configuration file is correctly parsed by get_config.
        """
        config = get_config("fake_path")
        mock_open.assert_called_with("fake_path", encoding="utf-8")
        mock_read.assert_called_once()

    @patch("os.environ.get", side_effect=lambda key: "env_value" if key == "VAR1" else None)
    @patch("configparser.ConfigParser.read", side_effect=lambda file, encoding: {"ENVIRONMENT": {"VAR1": "file_value"}})
    def test_get_config_env_overrides(self, mock_read, mock_environ):
        """
        Test if environment variables override file values in get_config.
        """
        config = get_config("fake_path")
        self.assertEqual(config["ENVIRONMENT"]["VAR1"], "env_value")  # env_value should override file_value

    @patch("builtins.open", mock_open())
    def test_get_logging_config_file_not_found(self):
        """
        Test if FileNotFoundError is raised when logging config file is missing.
        """
        with self.assertRaises(FileNotFoundError):
            get_logging_config("invalid_path")

    @patch("os.path.exists", return_value=False)
    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    @patch("logging.config.fileConfig")
    @patch("os.path.isdir", return_value=False)
    def test_configure_logging_creates_files(self, mock_isdir, mock_fileconfig, mock_open, mock_makedirs, mock_exists):
        """
        Test if configure_logging creates log files and directories when needed.
        """
        configure_logging()

        mock_isdir.assert_called_with("Logs")
        mock_makedirs.assert_called_once_with("Logs")
        mock_open.assert_any_call("Logs/traceback.log", "w")

    @patch("logging.StreamHandler")
    @patch("logging.FileHandler")
    @patch("logging.Formatter")
    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open, read_data="[handler_file]\nargs=logfile.log\nmode=w\nencoding=utf-8")
    @patch("configparser.ConfigParser.read", side_effect=lambda file, encoding: {"handler_file": {"args": "logfile.log", "mode": "w", "encoding": "utf-8"}})
    def test_configure_logging_handlers_set_up(self, mock_read, mock_open, mock_makedirs, mock_formatter, mock_filehandler, mock_streamhandler):
        """
        Test if logging handlers (file and console) are correctly set up in configure_logging.
        """
        logging_config = configure_logging()

        mock_streamhandler.assert_called_once()
        mock_filehandler.assert_called_once_with("logfile.log", mode="w", encoding="utf-8")
        mock_formatter.assert_called_once_with(fmt="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    unittest.main()
