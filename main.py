import unittest
import logging
import datetime

import dateutils


class TestUtil(unittest.TestCase):

    def test_logging(self):
        logging.debug('This is a debug log')
        logging.info('This is a info log')
        logging.warning('This is a warning log')
        logging.error('This is a error log')
        logging.critical('This is a critical log')

    def test_get_last_month_date(self):
        current_data: datetime.date = datetime.date.today()
        last_month_date = dateutils.get_last_month_date(current_data)
        logging.info('last month date:{}'.format(last_month_date))

    def test_get_previous_month_date(self):
        current_data: datetime.date = datetime.date.today()

        n: int = 1
        previous_month_date: datetime.date = dateutils.get_previous_month_date(current_data, n)
        log_msg = '上一个月日期：{}'.format(previous_month_date)
        logging.info(log_msg)

        n: int = 2
        previous_month_date: datetime.date = dateutils.get_previous_month_date(current_data, n)
        log_msg = '两个月前日期：{}'.format(previous_month_date)
        logging.info(log_msg)

        n: int = 0
        previous_month_date: datetime.date = dateutils.get_previous_month_date(current_data, n)
        log_msg = '当前日期：{}'.format(previous_month_date)
        logging.info(log_msg)

        n: int = -1
        previous_month_date: datetime.date = dateutils.get_previous_month_date(current_data, n)
        log_msg = '当前日期：{}'.format(previous_month_date)
        logging.info(log_msg)
