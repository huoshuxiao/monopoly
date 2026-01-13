import datetime
import random

from com.sun.monopoly.common import utils, consts
from com.sun.monopoly.config.logger import logger

tag = 'model'


def run():
    result = __run_ssq__()
    if result:
        return result


def __run_ssq__():
    # bonus_weekday = [2, 4, 7, 5]
    bonus_weekday = [1,2,3, 4, 5, 6,7]
    today = datetime.date.today()
    weekday = today.isoweekday()
    if weekday in bonus_weekday:
        df = utils.read_csv(utils.get_data_raw_ssq_file_path())
        no = max(df['no'].to_list()) + 1
        if weekday == 5:
            today = today + datetime.timedelta(days=2)

        # 随机次数
        count = __get_ssq_random_count__()
        __bonus__ = __do_ssq_bonus__(count)
        logger.info(r'<<{}>> no :: {}, day :: {}, bonus :: {}'.format(tag, no, today, __bonus__))
        return __bonus__


def __get_ssq_random_count__():
    # 定义区间范围 数据个数 >=45
    ranges = consts.RANDOM_RANGE_SSQ
    # logger.info(r'<<{}>> range :: {}'.format(tag, ranges))

    # numpy.random.choice() 从多个区间中选择一个值
    # 随机选择一个范围并从中生成一个随机整数。
    selected_range = random.choice(ranges)
    logger.info(r'<<{}>> range :: from {} to {}'.format(tag, selected_range[0], selected_range[1]))
    j = random.randint(selected_range[0], selected_range[1])
    return j


# 根据随机次数开奖
def __do_ssq_bonus__(i):
    __i__ = i
    t = ''
    while i > 0:
        i = i - 1
        r = ','.join(str(s) for s in sorted(utils.randoms(33, 6), reverse=False))
        b = ','.join(str(s) for s in sorted(utils.randoms(16, 1), reverse=False))
        t = r + ',' + b
    logger.info(r'<<{}>> ssq bonus :: {}, count :: {}'.format(tag, t, __i__))
    return t