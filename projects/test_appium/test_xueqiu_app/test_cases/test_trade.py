"""测试交易页面【含 webview 组件】"""
from pages.app_page import APP


class TestTrade:

    def setup(self):
        self.trade = APP().goto_main().goto_trade()

    def test_create_account(self):
        self.trade.create_a_stack_account("12345678910")

    def teardown(self):
        self.trade.quit()
