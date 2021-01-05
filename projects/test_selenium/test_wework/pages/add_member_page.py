from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.contacts_page import ContactsPage


class AddMemberPage(BasePage):
    """定义添加成员页面功能：保存并继续；保存；取消"""

    def input_member_info(self, name, account, phone, gender='1'):
        self._driver.find_element(By.ID, 'username').send_keys(name)
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys(account)
        self._driver.find_element(By.CSS_SELECTOR, 'input[value="{}"]'.format(gender)).click()
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys(phone)

    def save_and_add(self, name, account, phone, gender='1'):
        self.input_member_info(name, account, phone, gender)
        self._driver.find_elements(By.CSS_SELECTOR, '.js_btn_continue')[-1].click()
        return self

    def save(self, name, account, phone, gender='1'):
        self.input_member_info(name, account, phone, gender)
        self._driver.find_elements(By.CSS_SELECTOR, '.js_btn_save')[-1].click()
        return ContactsPage(self._driver)

    def cancel(self):
        self._driver.find_elements(By.CSS_SELECTOR, '.js_btn_cancel')[0].click()
        return ContactsPage(self._driver)

    @property
    def success_alert(self):
        return self._driver.switch_to.alert.text

