import logging.config

import yaml

from com.sun.monopoly.common import utils, consts

# 加载 YAML 配置文件
with open(utils.get_log_path(), 'r') as file:
    config = yaml.safe_load(file)

# 配置 logging 模块
logging.config.dictConfig(config)

# 创建日志记录器
logger = logging.getLogger(consts.APP_ID)