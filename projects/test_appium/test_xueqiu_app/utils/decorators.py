"""装饰器合集"""

from functools import wraps
from utils.logging_utils import logger


def popup_handle(method):
    """处理自动化过程中突然弹出的窗口"""
    @wraps(method)
    def inner(self, locator, value=""):
        _count = 0
        _max = 3
        try:
            return method(self, locator, value)
        except Exception as e:
            if _count > _max:
                logger.error('larger than max times')
                raise e
            for popup in self._popup_list:
                ret = self.find_all(popup)
                if ret:
                    logger.info(f' find popup {popup}')
                    ret[0].click()
                    return method(self, locator, value)
                continue
            _count += 1
    return inner







