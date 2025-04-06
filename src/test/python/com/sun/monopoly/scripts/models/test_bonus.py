from com.sun.monopoly.features import similarity


def test_bonus_001():
    __bonus__ = '03010,20030327,01,02,08,13,17,24,13'

    # 计算生成号码的相似度
    __similarity__ = similarity.ssq(__bonus__)
    for k, v in __similarity__.items():
        print('key :: {} value :: {}', k, v)
        # if k > 0.555556:

