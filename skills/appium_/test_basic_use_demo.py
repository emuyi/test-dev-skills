import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = dict(
    deviceName='Android Emulator',
    automationName='UiAutomator2',
    platformName='Android',
    platformVersion='11',
    appPackage='com.xueqiu.android',
    appActivity='com.xueqiu.android.view.WelcomeActivityAlias',
    unicodeKeyboard=True,
    resetKeyboard=True,
    noReset=True,
    dontStopAppOnRest=True,
    skipServerInstallation=True
)


class TestXueQiu:

    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(5)

    def test_uiautomator(self):
        self.driver.find_element(MobileBy.ID, 'tv_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('阿里')
        time.sleep(1)  # 特殊情况
        locator = (By.ID, 'name')
        self.driver.find_element(*locator).click()
        stack_price = self.driver.find_element\
            (By.XPATH, '//*[@text="09988"]/../../..//*[contains(@resource-id, "current_price")]').text
        assert float(stack_price) > 200

    def teardown(self):
        pass
        # time.sleep(10)
        # self.driver.quit()