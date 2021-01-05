"""
Singleton Logger

@author: Hideaki Yoshida
"""

import datetime
from pytz import timezone
from api.third_party_libraries.logger.sqlite_handler import write_log_to_sqlite

class Logger:

    _singleton_logger_instance = None

    def __new__(cls):
        if cls._singleton_logger_instance is None:
            cls._singleton_logger_instance = super(Logger, cls).__new__(cls)
        return cls._singleton_logger_instance

    # debug < info < warning < error < critical
    def debug(self, message):
        self.write_log(message, 'DEBUG')

    def info(self, message):
        self.write_log(message, 'INFO')

    def warning(self, message):
        self.write_log(message, 'WARNING')

    def error(self, message):
        self.write_log(message, 'ERROR')

    def critical(self, message):
        self.write_log(message, 'CRITICAL')

    """
    Mark- private
    """
    def write_log(self, message, log_level):
        date_format = "%Y-%m-%d %H:%M:%S %p %Z"
        time_zone = timezone('US/Pacific')
        current_date = datetime.datetime.now(time_zone).strftime(date_format)
        log_message = log_level + ' - ' + current_date + ' - ' + message
        print(log_message)
        write_log_to_sqlite(log_message)
