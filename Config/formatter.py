import logging


class Formatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, levels=None):
        super().__init__(fmt, datefmt)
        self.levels = levels or {}

    def format(self, record):
        record.levelprefix = self.levels.get(record.levelno, "")
        emoji = ""
        if record.levelno == logging.CRITICAL:
            emoji = "💣"
        elif record.levelno == logging.ERROR:
            emoji = "🔥"
        elif record.levelno == logging.WARNING:
            emoji = "⚠️"
        elif record.levelno == logging.INFO:
            emoji = "ℹ️"
        elif record.levelno == logging.DEBUG:
            emoji = "🔍"
        record.emoji = emoji
        return super().format(record)
