from pages.app_page import APP


class TestSearch:

    def setup(self):
        self.search = APP().goto_main().goto_search()

    def test_add_stack(self):
        self.search.search('京东')
        self.search.add_stack('JD')
        assert '已添加' in self.search.get_add_msg('JD')

    def teardown(self):
        self.search.quit()