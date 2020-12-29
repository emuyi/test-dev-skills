"""
bing page
"""
from poium import Page, NewPageElement
from base_page import Base


class BingPage(Base):
    """简略版本"""

    def __init__(self, driver):
        super().__init__(driver)

    def input(self, text):
        self.by_id('sb_form_q').send_keys(text)

    def click(self):
        self.by_id('sb_form_go').click()


# poium 版本
class BingPagePoium(Page):
    """poium 版本"""
    input = NewPageElement(id_='sb_form_q', timeout=2, describe='搜索框')
    button = NewPageElement(id_='sb_form_go', timeout=2, describe='搜索按钮')


