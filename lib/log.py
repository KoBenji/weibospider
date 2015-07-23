#!-*-coding:utf8-*-
__author__ = 'gpxlcj'
import logging as lg
import datetime as dt


#初始化日志信息
def init_log():
    date = dt.datetime.now()
    filename = str(date.year) + '-' + str(date.month) + '-' + str(date.day) + '.log'
    filename = 'logs/' + filename
    lg.basicConfig(
        level=lg.DEBUG,
        format='ID:%(process)d %(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename=filename,
        filemode='a'
    )


def lg_debug(record):
    lg.debug(record)
    return True


def lg_info(record):
    lg.info(record)
    return True


def lg_warning(record):
    lg.warning(record)
    return True