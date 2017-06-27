# -*- coding: utf-8 -*-
import datetime
import time
import functools


def strip_values(values):
    return list(map(lambda x: str.strip(x), values))


class StripValues(object):
    def __call__(self, values):
        return strip_values(values)


class StripAndJoin(object):
    def __call__(self, values):
        return ''.join(strip_values(values))


class DateStrToTimeStamp(object):
    def __call__(self, values):
        if len(values) < 1:
            return -1
        date_list = DateStrToTimeStamp.parse_origin_date(values[0])
        print(date_list)
        date_str = DateStrToTimeStamp.concat_date_str(date_list)
        return DateStrToTimeStamp.to_ms(date_str)

    @staticmethod
    def lint_date_str(date_str):
        return ''.join(date_str.split())

    @staticmethod
    def parse_origin_date(date_str):
        tmp = list()
        date_str = DateStrToTimeStamp.lint_date_str(date_str)
        if '-' in date_str:
            tmp = date_str.split('-')
            if len(tmp) < 3:
                tmp.append('1')
            return tmp
        year_index = date_str.find('年')
        if year_index is -1:
            tmp.append('1999')
        else:
            tmp.append(date_str[:year_index])
        month_index = date_str.find('月')
        if month_index is -1:
            tmp.append('1')
        else:
            tmp.append(date_str[year_index + 1:month_index])
        tmp.append('1')
        return tmp

    @staticmethod
    def concat_date_str(date_list):
        return '/'.join(date_list)

    @staticmethod
    def to_ms(date_string):
        dt = datetime.datetime.strptime(date_string, "%Y/%m/%d")
        return (time.mktime(dt.timetuple()) + (dt.microsecond / 1000000.0)) * 1000


class FirstInteger(object):
    def __call__(self, values):
        if len(values) < 1:
            return -1
        return int(values[0])

class FirstFloat(object):
    def __call__(self, values):
        if len(values) < 1:
            return -1
        return float(values[0])
