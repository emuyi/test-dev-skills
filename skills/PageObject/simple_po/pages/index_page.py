from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class IndexPage(BasePage):

    _url = 'https://work.weixin.qq.com/'

    @property
    def register(self):
        self._driver.find_element(By.LINK_TEXT, '立即注册').click()
        return RegisterPage(self._driver)

    @property
    def login(self):
        self._driver.find_element_by_link_text('企业登录').click()
        return LoginPage(self._driver)
