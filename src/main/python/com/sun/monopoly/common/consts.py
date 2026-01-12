APP_ID = 'monopoly'

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
FORMAT_DATE = '%Y%m%d'
FORMAT_TIME = '%H:%M:%S'

ROOT_PATH = 'lottery'
CONFIG_LOG_PATH = 'logging.yaml'
CONFIG_APP_PATH = 'application.yaml'

PATH_RAW_DATA = 'data/raw'
PATH_FEATURE_DATA = 'data/feature'
PATH_CONFIG = 'config'

FILE_SSQ = 'ssq'
FILE_DLT = 'dlt'
FILE_COUNT_SSQ = 'ssq_count'
FILE_SIMILARITY_SSQ = 'ssq_similarity'

FIELDS_SSQ = ['no', 'date', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue1']
FIELDS_DLT = ['no', 'date', 'red1', 'red2', 'red3', 'red4', 'red5', 'blue1', 'blue2']
FIELDS_COUNT = ['count', 'count_length']

# ranges = [(1, 10)]
RANGE_SSQ = [(1000000, 2000000), (2000000, 3000000), (3000000, 4000000), (4000000, 5000000), (5000000, 6000000),
          (6000000, 7000000), (7000000, 8000000), (8000000, 9000000), (9000000, 10000000),
          (10000000, 11000000), (11000000, 12000000), (12000000, 13000000), (13000000, 14000000), (14000000, 15000000),
          (15000000, 16000000), (16000000, 17000000), (17000000, 18000000), (18000000, 19000000), (19000000, 20000000),
          (20000000, 21000000), (21000000, 22000000), (22000000, 23000000), (23000000, 24000000), (24000000, 25000000),
          (25000000, 26000000),  # (26000000, 27000000), (27000000, 28000000),
          # (30000000, 31000000),
          (31000000, 32000000)  # , (33000000, 34000000)
          ]

SIMILARITY_SSQ_COUNT = 150