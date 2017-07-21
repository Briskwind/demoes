 # -*- coding: utf-8 -*-
import datetime
from dateutil.relativedelta import relativedelta


def days_ago_from_now(n, dawn=False):
    """ 距离当前时间的 n 天 """
    today = datetime.datetime.now()
    if dawn:
        today = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
    days_ago = today - datetime.timedelta(n)

    return today, days_ago


def months_ago_form_now(n, day_begin=False, month_begin=False):
    """ 距离当天 n 个月 """
    today = datetime.datetime.now()
    
    if day_begin:
        today = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
    
    if month_begin:
        today = datetime.datetime(today.year, today.month, 1, 0, 0, 0)
    
    months_ago = today - relativedelta(months=n)
    
    return today, months_ago





