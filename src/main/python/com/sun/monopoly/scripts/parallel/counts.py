# 次数
import math
import os
import sys
from concurrent import futures

from com.sun.monopoly.common import utils, consts
from com.sun.monopoly.features.parallel import counts


def __run_ssq_count__():
    fields = consts.FIELDS_SSQ + consts.FIELDS_COUNT
    df = utils.read_csv(utils.get_data_raw_ssq_file_path())

    # 确保date列是字符串类型
    df['date'] = df['date'].astype(str)

    # 筛选出日期为指定年份的记录
    # 使用 apply 方法结合 lambda 函数检查每行的日期是否以 years 数组中的任意一个年份开头
    df = df[df['date'].apply(lambda x: any(x.startswith(str(year)) for year in __years__))]

    thread_count = (os.cpu_count() + 1) * 2
    data_split_size = math.ceil(len(df) / thread_count)

    body = []
    # 如果任务是CPU密集型的，即主要涉及大量计算和数据处理，应该选择进程池，以充分利用多核处理器的并行计算能力。资源占用高。
    with futures.ProcessPoolExecutor(thread_count) as executor:
        fs = []
        for i in range(0, thread_count):
            start = data_split_size * i
            end = start + data_split_size
            if end > len(df):
                end = len(df)
            # 越界退出
            if end <= start:
                break

            f = executor.submit(counts.count, start, end, df)
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


__years__ = sys.argv[1].split(',')
if __name__ == '__main__':
    __run_ssq_count__()
