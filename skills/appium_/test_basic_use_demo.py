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

    def test_uiselector(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("5小时前").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

    def test_cancel_my_stacks(self):
        self.driver.find_element(MobileBy.ID, 'tv_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('茅台')
        self.driver.find_element(By.ID, 'name').click()
        self.driver.find_element(MobileBy.ID, 'followed_btn').click()
        follow_btn = (MobileBy.ID, 'follow_btn')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(follow_btn))
        assert '加自选' in self.driver.find_element(*follow_btn).text

    def teardown(self):
        time.sleep(10)
        self.driver.quit()