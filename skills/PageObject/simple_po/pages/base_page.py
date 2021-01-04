"""Base Page"""
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver = None):  # 添加注解 指定driver的类型，方便ide识别 self_driver ，更好的去调用相关的方法
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.get(self._url)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

    def quit(self):
        time.sleep(2)
        self._driver.quit()
