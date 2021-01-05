
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Base Page 处理 driver 相关操作"""

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                option = webdriver.ChromeOptions()
                option.debugger_address = '127.0.0.1:9222'
                self._driver = webdriver.Chrome(options=option)
            else:
                self._driver = webdriver.Chrome()
            self._driver.get(self._url)
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

    def quit(self):
        self._driver.quit()