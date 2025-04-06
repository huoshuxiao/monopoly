import pandas as pd

from com.sun.monopoly.common import utils


def test_run_last_ssq_count():
    df = utils.read_csv(utils.get_data_raw_ssq_file_path())
    # last data
    df1 = df[(len(df) - 1):len(df)]
    count = 1000000
    df1['count']=count
    df1['count_length']=len(str(count))
    # df2 = pd.DataFrame({
    #     'count': [count],
    #     'count_length': [len(str(count))],
    # })
    # result = pd.concat([df1, df2], axis=1, ignore_index=True)
    # print(result.values.tolist()[0])

    df1['count']=count
    df1['count_length']=len(str(count))
    print(df1.values.tolist()[0])
    file_name = '_'+ str(utils.year())
    utils.append_csv(str(utils.get_data_ssq_count_file_path()) + file_name, df1.values.tolist()[0])