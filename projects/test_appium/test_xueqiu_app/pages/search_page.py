"""search page"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):

    def search(self, search_keyword):
        self.find(By.ID, 'search_input_text').send_keys(search_keyword)
        self.find(By.ID, 'name').click()
        return self

    def get_stack_price(self, which_stack):
        stack_price = self.find\
            (By.XPATH, f'//*[@text="{which_stack}"]/../../..//*[contains(@resource-id, "current_price")]').text
        return float(stack_price)

    def add_stack(self, which_stack):
        add_btn = self.find\
            (By.XPATH, f'//*[@text="{which_stack}"]/../../..//*[contains(@resource-id, "follow_btn")]')
        add_btn.click()
        return self

    def get_add_msg(self, which_stack):
        # 检查添加股票自选后的信息
        added_btn = self.find\
            (By.XPATH, f'//*[@text="{which_stack}"]/../../..//*[contains(@resource-id, "followed_btn")]')
        return added_btn.text
