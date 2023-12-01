# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
# Добавьте возможность запуска из командной строки с использованием библиотеки argparse


import logging
import datetime
from datetime import date, datetime
from collections import namedtuple
from calendar import monthrange

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', type=str, help='дата в формате "1-й четверг ноября"')
args = parser.parse_args()



MONTH = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "марта": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12
}


WEEKDAYS = {
    "понедельник": 0,
    "вторник": 1,
    "среда": 2,
    "четверг": 3,
    "пятница": 4,
    "суббота": 5,
    "воскресенье": 6
}

logging.basicConfig(filename="log.log", encoding="utf8", level=logging.INFO)
logger = logging.getLogger("log")


DATE = namedtuple("DATE", "day mouth year")


def get_date(text):
    num_week, week_day, mounth = text.split()
    num_week = int(num_week.split("-")[0])
    week_day = WEEKDAYS[week_day]
    count_week = 0
    for day in range(1, 31+1):
        d = date(year=datetime.now().year, month=MONTH[mounth], day=day)
        if d.weekday() == week_day:
            count_week += 1
            if count_week == num_week:
                logger.info(DATE(d.day, d.month, d.year))
                return d
print(get_date(input("введите дату в формате '1-й четверг ноября': ")))

# def get_date():
#     text = args.text
#     if not text:
#         logger.warning("no --text provided")
#         return
#     try:
#         num_week, week_day, mounth = text.split()
#         num_week = int(num_week.split("-")[0])
#         week_day = WEEKDAYS[week_day]
#         month = MONTH[mounth]
#     except:
#         logger.warning("wrong --text format")
#         return

#     count_week = 0
#     year = datetime.now().year
#     for day in range(1, monthrange(year, month)[1] + 1):
#         d = date(year=year, month=month, day=day)
#         if d.weekday() == week_day:
#             count_week += 1
#         if count_week == num_week:
#             logger.info(DATE(d.day, d.month, d.year))
#             return
#     logger.warning("senseless request - this day doesn't exist")
#     return

# get_date()