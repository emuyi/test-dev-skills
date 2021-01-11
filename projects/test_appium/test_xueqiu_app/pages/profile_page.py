""" 我的页面 """
from pages.base_page import BasePage
from pages.loggin_page import LoginPage


class ProfilePage(BasePage):

    def goto_login(self):
        self.find_by_text('登录雪球').click()
        return LoginPage(self._driver)