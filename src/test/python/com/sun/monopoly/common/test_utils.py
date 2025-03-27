import random

from com.sun.monopoly.common import utils


def test_root():
    print(r'root path2 :: {}'.format(utils.__root__()))
    print(r'raw data path :: {}'.format(utils.__get_raw_data_path__()))
    print(r'length :: {}'.format(len(str(1234567))))


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
