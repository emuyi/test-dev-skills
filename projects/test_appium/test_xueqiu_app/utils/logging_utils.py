"""logging 工具"""

import os
import logging
from settings import Settings as ST
from utils.func_utils import make_dirs


class LoggingUtils:

    def __init__(self):
        make_dirs(ST.LOG_PATH)
        self._logger = logging.getLogger(__name__)
        file_path = os.path.join(ST.LOG_PATH, 'running_log.txt')
        fh = logging.FileHandler(file_path, encoding='utf-8')  # file handler 用于将日志输出到文件
        sh = logging.StreamHandler()  # stream handler 将日志输出到 console
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s - %(message)s', '%Y-%m-%d %H:%M:%S')  # 设置日志样式
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self._logger.setLevel(logging.DEBUG)  # 注意：logger 对象也是设置下 level，默认是 warning
        fh.setLevel(logging.INFO)  # 给 fh，sh 设置级别
        sh.setLevel(logging.INFO)
        self._logger.addHandler(fh)  # logger对象可以添加多个fh和sh对象
        self._logger.addHandler(sh)

    @property
    def logger(self):
        return self._logger


logger = LoggingUtils().logger
