# 次数
import math
import os
from concurrent import futures

from com.sun.monopoly.common import consts, utils
from com.sun.monopoly.config.logger import logger

tag = 'feature'


def run_ssq_count(years):
    fields = consts.FIELDS_SSQ + consts.FIELDS_COUNT
    df = utils.read_csv(utils.get_data_raw_ssq_file_path())

    # 确保date列是字符串类型
    df['date'] = df['date'].astype(str)

    # 筛选出日期为指定年份的记录
    # 使用 apply 方法结合 lambda 函数检查每行的日期是否以 years 数组中的任意一个年份开头
    df = df[df['date'].apply(lambda x: any(x.startswith(str(year)) for year in years))]

    thread_count = os.cpu_count() + 1
    data_split_size = math.ceil(len(df) / thread_count)

    body = []
    # 如果任务是I/O密集型的，即主要涉及网络通信、文件读写和数据库操作等，应该选择线程池，以充分利用线程的非阻塞特性，提高执行效率。
    with futures.ThreadPoolExecutor(thread_count) as executor:
        fs = []
        for i in range(0, thread_count):
            start = data_split_size * i
            end = start + data_split_size
            if end > len(df):
                end = len(df)
            # 越界退出
            if end <= start:
                break

            f = executor.submit(count, start, end, df)
            fs.append(f)

        for f in futures.as_completed(fs):
            for r in f.result():
                d = r.split(',')
                row = {
                    'no': d[0],
                    'date': d[1],
                    'red1': d[2],
                    'red2': d[3],
                    'red3': d[4],
                    'red4': d[5],
                    'red5': d[6],
                    'red6': d[7],
                    'blue1': d[8],
                    'count': d[9],
                    'count_length': len(d[9]),
                }
                body.append(row)

        utils.write_csv(utils.get_data_ssq_count_file_path(), fields, body)


def count(start, end, df):
    logger.info(r'<<{}>> start :: {}, end :: {}'.format(tag, start, end))
    result = []
    for i in range(start, end):
        no = str(df.iloc[i]['no'])
        date = str(df.iloc[i]['date'])
        red1 = str(df.iloc[i]['red1'])
        red2 = str(df.iloc[i]['red2'])
        red3 = str(df.iloc[i]['red3'])
        red4 = str(df.iloc[i]['red4'])
        red5 = str(df.iloc[i]['red5'])
        red6 = str(df.iloc[i]['red6'])
        blue1 = str(df.iloc[i]['blue1'])
        bonus = [','.join([red1, red2, red3, red4, red5, red6, blue1])]
        __count__ = __cal_ssq_count__(bonus)
        result.append(','.join([no, date, red1, red2, red3, red4, red5, red6, blue1, str(__count__)]))
    return result


# 指定号码的随机次数分析
def __cal_ssq_count__(bonuses):
    for bonus in bonuses:
        i = 0
        do = True
        while do:
            i = i + 1
            r = ','.join(str(s) for s in sorted(utils.randoms(33, 6), reverse=False))
            b = ','.join(str(s) for s in sorted(utils.randoms(16, 1), reverse=False))
            t = r + ',' + b
            if bonus == t:
                do = False

        logger.info(r'<<{}>> bonus :: {}, count :: {}'.format(tag, bonus, i))
        if not (len(str(i)) == 7 or len(str(i)) == 8):
            __cal_ssq_count__(bonuses)
            
        return i