import random

import pandas as pd

from com.sun.monopoly.common import utils


def test_root():
    print(r'root path2 :: {}'.format(utils.__root__()))
    print(r'raw data path :: {}'.format(utils.__get_raw_data_path__()))
    print(r'length :: {}'.format(len(str(1234567))))


def test_append_csv():
    body=pd.DataFrame({
        'no': '25033',
        'date': '20250327',
        'red1': '3',
        'red2': '5',
        'red3': '18',
        'red4': '25',
        'red5': '26',
        'red6': '33',
        'blue1': '8',
        'count': '9628577',
        'count_length': '7',
    },index=['no','date','red1','red2','red3','red4','red5','red6','blue1','count','count_length'])
    utils.append_csv('/home/sunwenkun/Developer/workspace/monopoly.git/data/feature/ssq_count_2025',body.values.tolist()[0]
                     # ['25033','20250327','3','5','18','25','26','33','8','9628577','7']
                     )


def test_random():
    # 定义范围
    ranges = [(1000000, 28000000), (30000000, 32000000), (33000000, 34000000)]

    # 随机选择一个范围并从中生成一个随机整数
    selected_range = random.choice(ranges)
    j = random.randint(selected_range[0], selected_range[1])

    # 判断 j 是否在任何一个给定的范围内
    if any(lower <= j <= upper for (lower, upper) in ranges):
        print(f"{j} 在指定的一个或多个范围内")
    else:
        print(f"{j} 不在任何指定的范围内")
