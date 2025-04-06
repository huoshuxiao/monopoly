import csv
import datetime
import os
import random
from pathlib import Path

import pandas
import pandas as pd

from com.sun.monopoly.common import consts


def __root__():
    """获取项目根目录"""
    return Path(__file__).resolve().parents[7]  # 调整数字以匹配你的目录层级


def __get_raw_data_path__():
    r"""get resources directory ."""
    return __root__() / consts.PATH_RAW_DATA


def __get_feature_data_path__():
    r"""get resources directory ."""
    return __root__() / consts.PATH_FEATURE_DATA


def __get_config_path__():
    return __root__() / consts.PATH_CONFIG


def get_log_path():
    return __get_config_path__() / consts.CONFIG_LOG_PATH


def get_app_path():
    return __get_config_path__() / consts.CONFIG_APP_PATH


def get_data_raw_ssq_file_path():
    return __get_raw_data_path__() / consts.FILE_SSQ


def get_data_raw_dlt_file_path():
    return __get_raw_data_path__() / consts.FILE_DLT


def get_data_ssq_count_file_path():
    return __get_feature_data_path__() / consts.FILE_COUNT_SSQ


def get_data_ssq_similarity_file_path():
    return __get_feature_data_path__() / consts.FILE_SIMILARITY_SSQ


def read_csv(file_path):
    file = r'{}.csv'.format(file_path)
    return pandas.read_csv(file)


def write_csv(file_path, fields, body):
    # name of csv file
    file = r'{}.csv'.format(file_path)

    with open(file, 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        writer.writerows(body)


def append_csv(file_path, body):
    # name of csv file
    file = r'{}.csv'.format(file_path)

    with open(file, 'a', encoding="utf-8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 写入新数据行
        writer.writerow(body)


def write_excel(file_path, sheet_name, df):
    file = r'{}.xlsx'.format(file_path)
    if not os.path.exists(file):
        df.to_excel(file, header=False, index=False, sheet_name=sheet_name)

    with pd.ExcelWriter(file, mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
        df.to_excel(writer, header=False, index=False, sheet_name=sheet_name)


def remove_excel(file_path):
    file = r'{}.xlsx'.format(file_path)
    if os.path.exists(file):
        os.remove(file)


def today():
    return datetime.date.today()


def year():
    return today().year


def is_work_day(target_day):
    _year = target_day.year
    _month = target_day.month
    _day = target_day.day
    date = datetime.date(_year, _month, _day)

    if date.weekday() == 5 or date.weekday() == 6:
        return False
    return True


def randoms(scope, count):
    return random.sample(range(1, scope + 1), count)


# return string randoms
def randoms_s(scope, count):
    r = randoms(scope, count)
    result = []
    for i in r:
        if i < 10:
            result.append(str(i).zfill(2))
        else:
            result.append(str(i))

    return result