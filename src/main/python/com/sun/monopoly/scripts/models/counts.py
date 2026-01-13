# 遥奖
from com.sun.monopoly.common import consts
from com.sun.monopoly.config.logger import logger
from com.sun.monopoly.features import similarity
from com.sun.monopoly.models import counts as bonus


# 相似度
def __cal_similarity__(__bonus__) -> str:
    tag = '__cal_similarity__'
    logger.info(r'<<{}>> , bonus :: {}'.format(tag, __bonus__))

    # 1.1 计算生成号码的相似度
    __similarity__ = max(sorted(similarity.ssq(__bonus__, None).items(), reverse=True))
    k = __similarity__[0]
    # for k, v in __similarity__.items():

    # # 相同个数:6,| 三等奖 | 5红1蓝 | 3000 |
    # if k >= 0.75:
    # 相同个数:5,| 四等奖 | 4红1蓝 | 200 |
    if k >= 0.55:
        __bonus__ = bonus.run()
        __cal_similarity__(__bonus__)
        # main()
    elif k < 0.4:
        logger.info(r'<<{}>> , bonus :: {} ==[{}]'.format(tag, __bonus__, 'OKOK'))
        return __bonus__
        # logger.info(r'ssq bonus finished1 :: {}'.format(__bonus__))
        # exit(0)

    # 1.2 计算生成号码的近100期相似度
    __similarity__ = max(sorted(similarity.ssq(__bonus__, consts.SIMILARITY_SSQ_COUNT).items(), reverse=True))
    k = __similarity__[0]
    # for k, v in __similarity__.items():

    # 相同个数:4 | 五等奖 | 4 红 or 3红1蓝 | 10 |
    if k >= 0.4:
        __bonus__ = bonus.run()
        __cal_similarity__(__bonus__)
        # main()
    else:
        logger.info(r'<<{}>> , bonus :: {} ==[{}]'.format(tag, __bonus__, 'OKOK'))
        return __bonus__
        # logger.info(r'ssq bonus finished2 :: {}'.format(__bonus__))
        # exit(0)


# 概率分布
def __cal_probability__(__bonus__) -> str:
    tag = '__cal_probability__'
    logger.info(r'<<{}>> , bonus :: {}'.format(tag, __bonus__))

    reds = __bonus__.split(',')[0:6]
    probability = 0
    # tuple to list (*)
    for i in range(0, 6):
        if int(reds[i]) in list(range(*consts.PROBABILITY_SSQ_RED[i])):
            probability = probability + 1

    if probability in range(4, 7):
        logger.info(r'<<{}>> , bonus :: {} ==[{}]'.format(tag, __bonus__, 'OKOK'))
        return __bonus__
    else:
        main()
        # __bonus__ = bonus.run()
        # # step 1, 重新计算
        # __cal_similarity__(__bonus__)


# 奇数偶数分布
def __cal_odd_even__(__bonus__) -> str:
    tag = '__cal_odd_even__'
    logger.info(r'<<{}>> , bonus :: {}'.format(tag, __bonus__))

    reds = __bonus__.split(',')[0:6]
    even = 0
    for i in range(0, 6):
        if __is_even__(reds[i]):
            even = even + 1

    if even in range(2, 5):
        logger.info(r'<<{}>> , bonus :: {} ==[{}]'.format(tag, __bonus__, 'OKOK'))
        return __bonus__
    else:
        main()
        # __bonus__ = bonus.run()
        # # step 1, 重新计算
        # __cal_similarity__(__bonus__)


# 偶数
def __is_even__(number) -> bool:
    if int(number) % 2 == 0:
        return True
    else:
        return False


def main():
    __bonus__ = bonus.run()

    # 1. 相似度
    __bonus__ = __cal_similarity__(__bonus__)

    # 2. 概率分布
    if __bonus__ is not None:
        __bonus__ = __cal_probability__(__bonus__)
    else:
        logger.error(r'error 1111111111111111')
        exit(1)

    # 3. 奇数偶数分布
    if __bonus__ is not None:
        __cal_odd_even__(__bonus__)
    else:
        logger.error(r'error 2222222222222222222')
        exit(1)


if __name__ == '__main__':
    main()
