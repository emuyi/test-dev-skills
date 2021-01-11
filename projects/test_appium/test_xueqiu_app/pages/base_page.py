""" Base Page"""
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from utils.decorators import popup_handle


class BasePage:

    _popup_list = [(By.ID, 'tv_left')]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def quit(self):
        self._driver.quit()

    @popup_handle
    def find(self, locator, value=""):
        """对原生 find_element 做封装"""
        return self._driver.find_element(*locator) if isinstance(locator, tuple) \
            else self._driver.find_element(locator, value)

    def find_all(self, locator, value=""):
        """对原生 find_elements 做封装"""
        return self._driver.find_elements(*locator) if isinstance(locator, tuple) \
            else self._driver.find_elements(locator, value)

    def find_by_text(self, text):
        """对使用 text 定位做的封装"""
        return self.find(By.XPATH, f'//*[@text="{text}"]')

    @property
    def toast_msg(self):
        """获取 toast 上的消息"""
        return self.find(By.XPATH, '//*[@class=android.widget.Toast]').text
