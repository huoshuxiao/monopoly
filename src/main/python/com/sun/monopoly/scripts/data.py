import warnings
from com.sun.monopoly.data import data

# 忽略所有 FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    data.run()