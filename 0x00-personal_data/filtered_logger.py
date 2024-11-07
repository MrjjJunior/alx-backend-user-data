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
        org_msg = super().format(record)
        return filter_datum(
            self.fields,
            elf.REDACTION,
            org_msg,
            self.SEPARATOR
            )


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
                ) -> str:
    '''Filter'''
    for field in fields:
        regex = f"{field}=[^{separator}]*"
        message = re.sub(regex, f"{field}={redaction}", message)
    return message
