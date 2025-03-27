import pandas as pd
import glob

def test01():

    # 获取所有待合并的csv文件列表
    # 这里使用glob模块来查找匹配的文件名模式
    all_files = glob.glob('/home/sunwenkun/Developer/workspace/data/lottery/ssq_count_*.csv')  # 修改为你的CSV文件所在目录路径

    # 创建一个空列表用于存储每个文件的数据帧
    dfs = []

    # 循环遍历每个文件，并将其读入数据帧中，然后添加到列表
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        dfs.append(df)

    # 使用pd.concat方法沿axis=0方向（即纵向）合并所有数据帧
    combined_df = pd.concat(dfs, axis=0, ignore_index=True)

    # 将合并后的数据帧保存到新的CSV文件中
    combined_df.to_csv('/home/sunwenkun/Developer/workspace/monopoly.git/data/feature/ssq_count.csv', index=False)  # 修改为你希望保存的路径和文件名