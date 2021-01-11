"""首页功能测试用例"""
from pages.app_page import APP


class TestMain:

    def setup(self):
        self.main = APP().goto_main()

    def test_search(self):
        stacks = self.main.goto_search().search('茅台')
        stack_price = stacks.get_stack_price('SH600519')
        assert stack_price > 2000

    def teardown(self):
        self.main.quit()