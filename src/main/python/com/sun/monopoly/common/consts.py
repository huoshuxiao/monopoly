APP_ID = 'monopoly'

ROOT_PATH = 'lottery'
CONFIG_LOG_PATH = 'logging.yaml'
CONFIG_APP_PATH = 'application.yaml'

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
FORMAT_DATE = '%Y%m%d'
FORMAT_TIME = '%H:%M:%S'

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