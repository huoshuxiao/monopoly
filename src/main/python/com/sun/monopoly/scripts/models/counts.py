# 遥奖
import asyncio

from com.sun.monopoly.common import consts
from com.sun.monopoly.config.logger import logger
from com.sun.monopoly.features import similarity
from com.sun.monopoly.models import counts as bonus


# 相似度
async def __cal_similarity__(__bonus__) -> int:
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
        return 0
    elif k < 0.4:
        logger.info(r'<<{}>> , bonus :: {} ==[{}]'.format(tag, __bonus__, 'OKOK1'))
        return 1
    else: # k == 0.4
        # 1.2 计算生成号码的近100期相似度
        __similarity__ = max(sorted(similarity.ssq(__bonus__, consts.SIMILARITY_SSQ_COUNT).items(), reverse=True))
        k = __similarity__[0]

        # 相同个数:4 | 五等奖 | 4 红 or 3红1蓝 | 10 |
        if k >= 0.4:
            return 0
        else:
            logger.info(r'<<{}>> , bonus :: {} ==[{}]'.format(tag, __bonus__, 'OKOK1'))
            return 1


# 概率分布
async def __cal_probability__(__bonus__) -> int:
    tag = '__cal_probability__'
    logger.info(r'<<{}>> , bonus :: {}'.format(tag, __bonus__))

    reds = __bonus__.split(',')[0:6]
    probability = 0
    # tuple to list (*)
    for i in range(0, 6):
        if int(reds[i]) in list(range(*consts.PROBABILITY_SSQ_RED[i])):
            probability = probability + 1

    if probability in range(4, 7):
        logger.info(r'<<{}>> , bonus :: {} ==[{}]'.format(tag, __bonus__, 'OKOK2'))
        return 1
    else:
        return 0


# 奇数偶数分布
async def __cal_odd_even__(__bonus__) -> int:
    tag = '__cal_odd_even__'
    logger.info(r'<<{}>> , bonus :: {}'.format(tag, __bonus__))

    reds = __bonus__.split(',')[0:6]
    even = 0
    for i in range(0, 6):
        if __is_even__(reds[i]):
            even = even + 1

    if even in range(2, 5):
        logger.info(r'<<{}>> , bonus :: {} ==[{}]'.format(tag, __bonus__, 'OKOK3'))
        return 1
    else:
        return 0


# 偶数
def __is_even__(number) -> bool:
    if int(number) % 2 == 0:
        return True
    else:
        return False


# 封装主逻辑的异步函数
async def main():
    while True:  # 使用无限循环替代递归
        __bonus__ = bonus.run()

        # 创建三个协程任务，但不立即执行
        # 1. 相似度
        task1 = asyncio.create_task(__cal_similarity__(__bonus__))

        # 2. 概率分布
        task2 = asyncio.create_task(__cal_probability__(__bonus__))

        # 3. 奇数偶数分布
        task3 = asyncio.create_task(__cal_odd_even__(__bonus__))

        # 并发等待所有任务完成
        # asyncio.gather 会返回一个包含所有任务返回值的列表
        results = await asyncio.gather(task1, task2, task3)

        point1, point2, point3 = results  # 解包结果
        total_points = point1 + point2 + point3 #计分

        logger.info(f"Bonus: {__bonus__}. Points: 相似度={point1}, 概率分布={point2}, 奇数偶数分布={point3}, Total={total_points}")
        if total_points == 3:
            logger.info(f"Bonus: {__bonus__}.")
            break  # 退出循环


if __name__ == '__main__':
    # 运行顶级异步函数
    asyncio.run(main())
