"""测试登录页面功能"""
from pages.app_page import APP


class TestLoginPage:

    def setup(self):
        self.login = APP().goto_main().goto_profile().goto_login()

    def test_login_by_passwd(self):
        login = self.login.login_by_passwd('asdfafsdfa', 'safsdjfoasjdofa')
        assert '错误' in login.login_msg

    def teardown(self):
        self.login.quit()