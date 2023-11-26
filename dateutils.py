import time
import datetime
import calendar


def get_last_month_date(date: datetime.date):
    """
    获取给定日期的上一个月的最后一天的日期
    :param date:
    :return:
    """
    date = date.replace(day=1)
    last_month_date: datetime.date = date - datetime.timedelta(days=1)
    return last_month_date


def get_previous_month_date(date: datetime.date, n: int = 1):
    """
    获取给定日期的N个月前的最后一天的日期
    :param date:
    :param n:
    :return:
    """
    for _ in range(n):
        date = get_last_month_date(date)
    return date
