import unittest
import logging
import datetime

import dateutils
import urlutils


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

    def test_url_quote(self):
        example: str = '你好'
        result: str = urlutils.url_quote(example)
        log_msg = result
        logging.info(log_msg)

    def test_url_unquote(self):
        example: str = '%E4%BD%A0%E5%A5%BD'
        result: str = urlutils.url_unquote(example)
        log_msg = result
        logging.info(log_msg)

    def test_url_params_dict_to_str(self):
        request_params = {'name': '小明', 'age': 18, 'page': 0, 'size': 10}
        result: str = urlutils.url_params_dict_to_str(request_params)
        log_msg = '转换后的结果: {}'.format(result)
        logging.info(log_msg)

    def test_url_params_str_to_dict(self):
        params_str = 'name=小明&age=18&page=0&size=10'
        result = urlutils.url_params_str_to_dict(params_str)
        log_msg = '转换后的结果: {}'.format(result)
        logging.info(log_msg)

        params_str = 'name=小明&name=小红&age=18&page=0&size=10'
        result = urlutils.url_params_str_to_dict(params_str)
        log_msg = '转换后的结果: {}'.format(result)
        logging.info(log_msg)

    def test_get_url_path(self):
        request_url = 'https://eva2.csdn.net/v3/example/lts/groups/logs'
        result = urlutils.get_url_path(request_url)
        log_msg = '请求路径: {}'.format(result)
        logging.info(log_msg)

    def test_get_url_query(self):
        request_url = 'https://eva2.csdn.net/v3/example/lts/groups/logs'
        result = urlutils.get_url_query(request_url)
        log_msg = '查询参数: {}'.format(result)
        logging.info(log_msg)

        request_url = 'https://eva2.csdn.net/v3/example/lts/groups/logs?name=小明&name=小红&age=18&page=0&size=10'
        result = urlutils.get_url_query(request_url)
        log_msg = '查询参数: {}'.format(result)
        logging.info(log_msg)
