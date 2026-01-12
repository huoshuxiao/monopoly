# 遥奖
from com.sun.monopoly.common import consts
from com.sun.monopoly.config.logger import logger
from com.sun.monopoly.features import similarity
from com.sun.monopoly.models import counts as bonus


def main():

    __bonus__ = bonus.run()

    # 1. 计算生成号码的相似度
    __similarity__ = max(sorted(similarity.ssq(__bonus__, None).items(), reverse=True))
    k = __similarity__[0]
    # for k, v in __similarity__.items():

    # # 相同个数:6,| 三等奖 | 5红1蓝 | 3000 |
    # if k >= 0.75:
    # 相同个数:5,| 四等奖 | 4红1蓝 | 200 |
    if k >= 0.55:
        main()
    elif k < 0.4:
        logger.info(r'ssq bonus finished1 :: {}'.format(__bonus__))
        exit(0)

    # 2. 计算生成号码的近100期相似度相
    __similarity__ = max(sorted(similarity.ssq(__bonus__, consts.SIMILARITY_SSQ_COUNT).items(), reverse=True))
    k = __similarity__[0]
    # for k, v in __similarity__.items():

    # 相同个数:4 | 五等奖 | 4 红 or 3红1蓝 | 10 |
    if k >= 0.4:
        main()
    else:
        logger.info(r'ssq bonus finished2 :: {}'.format(__bonus__))
        exit(0)

    # 3. 概率分布


    # 4. 奇数偶数分布


if __name__ == '__main__':
    main()
