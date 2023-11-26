import unittest
import logging


class TestUtil(unittest.TestCase):

    def test_logging(self):
        logging.debug('This is a debug log')
        logging.info('This is a info log')
        logging.warning('This is a warning log')
        logging.error('This is a error log')
        logging.critical('This is a critical log')
