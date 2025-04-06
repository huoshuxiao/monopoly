# 数据爬取

import requests
from bs4 import BeautifulSoup

from com.sun.monopoly.common import utils, consts
from com.sun.monopoly.config.logger import logger

url = 'http://datachart.500.com/ssq/history/newinc/history.php?start=03001&end=99999&sort=1'
tag = 'data'

def run():
    data = agent()
    utils.write_csv(utils.get_data_raw_ssq_file_path(), consts.FIELDS_SSQ, data)
    logger.info(r'<<{}>> {} :: {}'.format(tag, 'ssq', data[-1]))


def agent():
    r"""agent ssq data. """

    r = requests.get(url)
    html = BeautifulSoup(r.text, 'lxml')
    tr = html.select("#tdata tr")

    result = []
    # result = list()

    for item in tr:

        td = item.contents
        # data = dict()

        data = {
            # 期号
            'no': td[1].text,
            # 开奖日期
            'date': td[16].text.replace("-", ''),
            # 红球号码(6)[1-33]
            'red1': td[2].text,
            'red2': td[3].text,
            'red3': td[4].text,
            'red4': td[5].text,
            'red5': td[6].text,
            'red6': td[7].text,
            # 蓝球号码(1)[1-16]
            'blue1': td[8].text,
        }

        result.append(data)

    return result