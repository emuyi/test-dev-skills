"""
交易页面功能
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class TradePage(BasePage):

    def switch_context(self):
        contexts = self._driver.contexts
        WebDriverWait(self._driver, 10).until(lambda x: len(contexts) > 1)
        self._driver.switch_to.context(contexts[-1])
        return self

    def create_a_stack_account(self, username):
        self.switch_context()
        self.find(By.CSS_SELECTOR, "div[class^='trade_home_info']").click()
        WebDriverWait(self._driver, 10).until(lambda x: len(self._driver.window_handles) > 3)
        self._driver.switch_to.window(self._driver.window_handles[-1])
        phone = (By.CSS_SELECTOR, '#phone-number')
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(phone))
        self.find(phone).send_keys(username)



