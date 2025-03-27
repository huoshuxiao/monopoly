import datetime

import pandas as pd

from com.sun.monopoly.common import utils, consts
from com.sun.monopoly.config.logger import logger


# 最新（最新一期与之前数据的相似度）


# 生成号码与之前数据的相似度
def ssq(bonus):
    df = utils.read_csv(utils.get_data_raw_ssq_file_path())
    red1 = df['red1'].to_list()
    red2 = df['red2'].to_list()
    red3 = df['red3'].to_list()
    red4 = df['red4'].to_list()
    red5 = df['red5'].to_list()
    red6 = df['red6'].to_list()
    blue1 = df['blue1'].to_list()
    date = df['date'].to_list()

    red_data = []
    blue_data = []
    for i in range(0, len(red1)):
        row = [str(red1[i]), str(red2[i]), str(red3[i]), str(red4[i]), str(red5[i]), str(red6[i])]
        red_data.append(','.join(row))

        row = [str(blue1[i])]
        blue_data.append(','.join(row))

    result = []
    i = len(red_data)
    red_text = red_data[0:i]
    blue_text = blue_data[0:i]

    bonus_date = datetime.date.today().strftime(consts.FORMAT_DATE)

    # 计算相似度
    for j in range(0, len(red_text) - 1):
        pool_data = red_text[j] + ',B' + blue_text[j]
        bonus_data = ','.join(bonus.split(',')[0:6]) + ',B' + ','.join(bonus.split(',')[6:7])
        score = __similarity_score_(pool_data, bonus_data)
        print("日期：{} 当期号码：{} 池号码：{} 相似度得分:{} ".format(bonus_date, bonus_data.replace('B', ''), pool_data.replace('B', ''), score))
        # logger.info("日期：{} 当期号码：{} 池号码：{} 相似度得分:{} ".format(bonus_date, bonus_data.replace('B', ''), pool_data.replace('B', ''), score))

        data = {
            'date': bonus_date,
            'current': bonus_data.replace('B', ''),
            'pool': pool_data.replace('B', ''),
            'score': score,
            '_date': date[j],
        }
        result.append(data)

    utils.write_csv(str(utils.get_data_ssq_similarity_file_path()) + '_' + bonus_date, ['date', 'current', 'pool', 'score', '_date'], result)
    # 各相似度 数量
    # print(pd.DataFrame.from_records(result)['score'].value_counts())
    logger.info('各相似度 数量 :: \n%s', pd.DataFrame.from_records(result)['score'].value_counts().to_string())


# Jaccard相似度通过计算两个集合之间的交集和并集之间的比率来衡量相似性。
def __similarity_score_(arr1, arr2):
    set1 = set(arr1.split(","))
    set2 = set(arr2.split(","))
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    score = len(intersection) / len(union)
    return score