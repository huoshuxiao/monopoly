from com.sun.monopoly.common import utils


def test_root():
    print(r'root path2 :: {}'.format(utils.__root__()))
    print(r'raw data path :: {}'.format(utils.__get_raw_data_path__()))