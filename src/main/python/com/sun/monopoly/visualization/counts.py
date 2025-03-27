import matplotlib
import pandas as pd

from com.sun.monopoly.config.logger import logger

matplotlib.use('TkAgg')

from matplotlib import pyplot as plt

from com.sun.monopoly.common import utils

tag = 'visualization'

def draw_ssq():
    file_name = '_2025'
    df = utils.read_csv(str(utils.get_data_ssq_count_file_path()) + file_name)
    # df = utils.read_csv(utils.get_data_ssq_count_file_path())
    data = df['count']

    # 计算每百万区间内的数据个数
    # 这里我们使用pd.cut函数来创建bins，并计算每个bin中的值的数量
    bins = range(1000000, data.max() + 1000000, 1000000)
    counts_per_million = pd.cut(data, bins=bins).value_counts().sort_index()

    # 打印每条数据及其对应的计数
    for interval, count in counts_per_million.items():
        # print(f"区间 {interval}: 数据个数 = {count}")
        logger.info(f"区间 {interval}: 数据个数 = {count}")

    # 直方图（Histogram）
    counts, bins, patches = plt.hist(data, bins=bins, alpha=0.7, color='blue', edgecolor='black')
    # 在每个条形上方添加文本标签
    for count, patch in zip(counts, patches):
        height = patch.get_height()
        plt.text(patch.get_x() + patch.get_width() / 2., height, f'{int(count)}', ha='center', va='bottom')

    # 设置X轴的刻度标签为每个区间的起始值
    bin_start = bins[:-1]  # 每个区间的起始值
    plt.xticks(bin_start, [f'{x:.0f}' for x in bin_start], rotation=45, ha='right')  # 显示实际数据值
    #plt.xticks(bin_start, [f'{x / 1e6:.0f}M' for x in bin_start], rotation=45, ha='right')  # 显示实际数据值并转换为'M'表示百万

    plt.title('SSQ COUNTS')
    plt.xlabel('Values')    # X轴标签：值
    plt.ylabel('Frequency') # Y轴标签：频率/次数
    plt.tight_layout()  # 调整布局以避免标签重叠
    plt.show()


if __name__ == '__main__':
    draw_ssq()
