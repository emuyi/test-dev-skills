"""
Toast: Android中一种消息提示的方式, 如 微信的没有找到网络的提示，它是一个浮动的显示框，显示后超时会自动消失。
所以定位 Toast 有两种方式：
    1. 使用 toast 的 class 属性定位 //*[@class="android.widget.Toast"]
    2. 可以用 toast 消息提示的 text 定位(//*[contains(@text, "xxx")])但如果其他控件有相同的 text，就会出问题
"""

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = dict(
    deviceName='android emulator',
    automationName='uiautomator2',
    platformName='android',
    paltformVersion='10',
    appPackage='tv.danmaku.bili',
    appActivity='tv.danmaku.bili.ui.splash.SplashActivity',
)


class TestBilibiliLogin:

    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)

    def test_login(self):
        self.driver.find_element(By.ID, 'agree').click()
        login = (By.ID, 'avatar')
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(login))
        self.driver.find_element(*login).click()
        self.driver.find_element(By.XPATH, '//*[@text="密码登录" and contains(@resource-id, "button")]').click()
        self.driver.find_element(By.ID, 'username').send_keys('sdfas')
        self.driver.find_element(By.ID, 'userpwd').send_keys('sfsadfas')
        self.driver.find_element(By.ID, 'btn_login').click()
        msg_toast = self.driver.find_element(By.XPATH, '//*[@class="android.widget.Toast"]').text
        assert '错误' in msg_toast

    def teardown(self):
        self.driver.quit()



