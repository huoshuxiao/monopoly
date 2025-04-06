# 遥奖
from com.sun.monopoly.features import similarity
from com.sun.monopoly.models import counts as bonus


def main():
    __bonus__ = bonus.run()

    # 计算生成号码的相似度
    __similarity__ = similarity.ssq(__bonus__)
    for k, v in __similarity__.items():
        # print(r'key :: {} value :: {}', k, v)
        if k > 0.555556:
            main()
    # 概率

if __name__ == '__main__':
    main()
