"""
简写，以实现功能为主，不做文件及细节上的区分
"""
import pytest
from appium import webdriver

app_caps = {
    'deviceName': 'Android Emulator',
    'automationName': 'appium',
    'platformName': 'Android',
    'platformVersion': '11',
    'appPackage': 'tv.danmaku.bili',
    'appActivity': 'tv.danmaku.bili.ui.splash.SplashActivity',
    'noRest': True

}


@pytest.fixture
def driver():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', app_caps)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


