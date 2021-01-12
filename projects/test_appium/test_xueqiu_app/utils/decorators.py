"""装饰器合集"""
import os
import yaml
from functools import wraps, partial
from utils.logging_utils import logger
from settings import Settings as ST


def popup_handle(method):
    """处理自动化过程中突然弹出的窗口"""
    @wraps(method)
    def inner(self, locator, value=""):
        try:
            return method(self, locator, value)
        except Exception as e:
            for popup in self._popup_list:
                ret = self.find_all(popup)
                if ret:
                    logger.info(f' find popup {popup}')
                    ret[0].click()
                    return method(self, locator, value)
                continue
            raise e
    return inner







