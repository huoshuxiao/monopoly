import pandas as pd

from com.sun.monopoly.common import utils
from com.sun.monopoly.config.logger import logger
from com.sun.monopoly.features.parallel import counts


# last data count
def run_last_ssq_count():
    df = utils.read_csv(utils.get_data_raw_ssq_file_path())
    # last data
    df1 = df[(len(df) - 1):len(df)]
    bonus_count = counts.count(len(df) - 1, len(df), df)
    count = bonus_count[0].split(',')[-1]
    # df2 = pd.DataFrame({
    #     'count': [count],
    #     'count_length': [len(str(count))],
    # })
    logger.info(r'<<{}>> bonus :: {}'.format("test_count", bonus_count[0]))
    file_name = '_'+ str(utils.year())
    # 水平拼接（添加列）
    df1['count']=count
    df1['count_length']=len(str(count))
    # result = pd.concat([df1, df2], axis=1)
    # utils.append_csv(str(utils.get_data_ssq_count_file_path()) + file_name, result.values.tolist()[0])
    utils.append_csv(str(utils.get_data_ssq_count_file_path()) + file_name, df1.values.tolist()[0])