import os
from loguru import logger
from datetime import datetime
from enum import Enum

# Custom Logger. Basically based on loguru but easier for me to setup.

base_dir = os.path.dirname(os.path.abspath(__file__))

today = datetime.now().strftime("%Y-%m-%d")

log_file = os.path.join(base_dir, "../logs", f"{today}.log")

os.makedirs(os.path.dirname(log_file), exist_ok=True)

logger.add(
    log_file, 
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", 
    level="DEBUG", 
    rotation="100 MB", 
    compression="zip", 
    retention="10 days"
)

class LogLevels(Enum):
    INFO = 1
    DEBUG = 2
    ERROR = 3

class Logger:

    @staticmethod
    def log(message, level):
        if not isinstance(message, str):
            raise Exception("Message is not a valid string.")
        if not isinstance(level, LogLevels):
            raise Exception("Log Level is not a valid level.")
        if message == None or message == "":
            raise Exception("Log needs message.")

        if level == LogLevels.INFO:
            logger.info(message)
        elif level == LogLevels.DEBUG:
            logger.debug(message)
        elif level == LogLevels.ERROR:
            logger.error(message)
