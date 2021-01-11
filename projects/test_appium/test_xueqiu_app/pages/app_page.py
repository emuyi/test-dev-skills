""" Android App Page"""

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.main_page import MainPage


class APP(BasePage):

    def __init__(self, driver: WebDriver = None):
        """这里选择重写 basePage init，而不是在 basePage中设置 driver，原因出于多平台的考虑"""
        super().__init__(driver)
        # 因为目前只涉及单个平台，暂不将caps做解耦处理
        if driver is None:
            desired_caps = dict(
                deviceName='android emulator',
                automationName='uiautomator2',
                platformName='android',
                appPackage='com.xueqiu.android',
                appActivity='com.xueqiu.android.view.WelcomeActivityAlias',
                unicodeKeyboard=True,
                resetKeyboard=True,
                chromedriverExecutableDir=r'D:\android-chromedriver'
            )
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        else:
            # 如果 driver 已经存在，那就应该直接启动 app，即复用原有的driver
            self._driver.start_activity('com.xueqiu.android', 'com.xueqiu.android.view.WelcomeActivityAlias')
        self._driver.implicitly_wait(5)

    def stop_app(self):
        self._driver.close_app()
        return self

    def restart_app(self):
        self._driver.launch_app()
        return self

    def background(self, time):
        self._driver.background_app(time)
        return self

    def lock_app(self, time):
        self._driver.lock(time)

    def goto_main(self):
        # 需要设置等待主页面加载完成
        WebDriverWait(self._driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@text="雪球"]')))
        return MainPage(self._driver)
