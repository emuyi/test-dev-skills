"""
登录页面
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    def login_by_passwd(self, username, passwd):
        self.find(By.ID, 'login_account').send_keys(username)
        self.find(By.ID, 'login_password').send_keys(passwd)
        self.find(By.ID, 'button_next').click()
        return self

    @property
    def login_msg(self):
        return self.find(By.ID, 'md_content').text
