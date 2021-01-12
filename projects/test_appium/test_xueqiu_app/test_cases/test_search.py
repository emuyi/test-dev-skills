import yaml
import pytest
from pages.app_page import APP

# todo 放在哪里比较合适，如果做成类似 ddt @file_data 的形式该怎么处理【关键在于怎么可以mark.parametrize进行配合】
# with open('../data/test_search.yml', encoding='utf-8') as f:
#     data = yaml.safe_load(f)


class TestSearch:

    def setup(self):
        self.search = APP().goto_main().goto_search()

    # def test_add_stack(self):
    #     self.search.search('京东')
    #     self.search.add_stack('JD')
    #     assert '已添加' in self.search.get_add_msg('JD')

    # @pytest.mark.parametrize('keyword, stack', data)
    # def test_add_stack(self, keyword, stack):
    #     self.search.search(keyword)
    #     self.search.add_stack(stack)
    #     assert '已添加' in self.search.get_add_msg(stack)

    def teardown(self):
        self.search.quit()

