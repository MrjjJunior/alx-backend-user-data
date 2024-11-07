#!/usr/bin/env python3
""" filter """
from typing import List, Union
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, original_message, self.SEPARATOR)


def filter_datum(fields: List[str],
                redaction: str,
                message: str,
                separator: str
                ) -> str:
    '''Returns log message'''
    #pattern = f'({"|".join(fields)})=[^;]*'
    #replacement = rf"\1={redaction}"
    #return re.sub(pattern, replacement, message)
    for field in fields:
        regex = f"{field}=[^{separator}]*"
        message = re.sub(regex, f"{field}={redaction}", message)
    return message