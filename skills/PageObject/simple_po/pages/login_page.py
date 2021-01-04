"""Login Page"""
from pages.base_page import BasePage
from pages.register_page import RegisterPage


class LoginPage(BasePage):

    def login_qrcode(self):
        pass

    def goto_register(self):
        self._driver.find_element_by_link_text('企业注册').click()
        return RegisterPage(self._driver)

