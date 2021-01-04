import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class RegisterPage(BasePage):

    def register(self, corp_name):
        self._driver.find_element(By.ID, 'corp_name').send_keys(corp_name)
        self._driver.find_element(By.ID, 'iagree').click()
        self._driver.find_element(By.ID, 'submit_btn').click()
        return self   # 这块其实应该分两种去情况考虑，如果是错误信息返回self，如果是正确信息返回正确的PO

    def get_error_msg(self):
        error_msg_locator = (By.CSS_SELECTOR, ".js_error_msg")
        return [msg.text for msg in self._driver.find_elements(*error_msg_locator)]

