
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

desired_caps = dict(
    deviceName='Android Emulator',
    automationName='UiAutomator2',
    platformName='Android',
    platformVersion='11',
    appPackage='com.xueqiu.android',
    appActivity='com.xueqiu.android.view.WelcomeActivityAlias',
    unicodeKeyboard=True,
    resetKeyboard=True
)


class TestXueQiu:

    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(5)

    def test_uiautomator(self):
        self.driver.find_element(MobileBy.ID, 'tv_search').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH, '//*[@text="阿里巴巴"]').click()
        stack_price = self.driver.find_element(By.XPATH, '//*[@text="09988"]/../[3]').text
        print(stack_price)
        assert int(stack_price) > 200


    def teardown(self):
        pass