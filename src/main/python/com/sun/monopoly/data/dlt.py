# 数据爬取

import csv

import requests
from bs4 import BeautifulSoup

from com.sun.monopoly.common import utils, consts

url = 'http://datachart.500.com/dlt/history/newinc/history.php?start=03001&end=99999&sort=1'


def run():
    data = agent()
    utils.write_csv(utils.get_data_raw_dlt_file_path(), consts.FIELDS_DLT, data)


def agent():
    r"""agent dlt data. """

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
            'date': td[15].text.replace("-", ''),
            # 红球号码(5)[1-35]
            'red1': td[2].text,
            'red2': td[3].text,
            'red3': td[4].text,
            'red4': td[5].text,
            'red5': td[6].text,
            # 蓝球号码(2)[1-12]
            'blue1': td[7].text,
            'blue2': td[8].text,
        }

        result.append(data)

    return result