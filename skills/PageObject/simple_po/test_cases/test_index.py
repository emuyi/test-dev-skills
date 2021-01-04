from pages.index_page import IndexPage


class TestIndex:
    """测试企业微信首页"""

    def setup_method(self):
        self.index_page = IndexPage()

    def test_register(self):
        """测试注册功能"""
        register_page = self.index_page.register.register('EMUYI')
        error_msg = register_page.get_error_msg()
        assert '请选择' in ':'.join(error_msg)

    def test_login(self):
        """从登录页面进行注册"""
        self.index_page.login.goto_register()

    def teardown_method(self):
        self.index_page.quit()