from pages.add_member_page import AddMemberPage
from pages.base_page import BasePage

from selenium.webdriver.common.by import By

from pages.contacts_page import ContactsPage
from pages.import_contact_page import ImportContactPage
from pages.send_message_page import SendMessagePage


class AdminPage(BasePage):
    """定义 admin 页面业务功能"""

    _url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def __init__(self):
        super().__init__(reuse=True)

    def add_member(self):
        self._driver.find_element(By.CSS_SELECTOR, '.js_service_list > a:nth-child(1)').click()
        return AddMemberPage(self._driver)

    def import_contact(self):
        self._driver.find_element(By.CSS_SELECTOR, '.js_service_list > a:nth-child(2)').click()
        return ImportContactPage(self._driver)

    def send_message(self):
        self._driver.find_element(By.CSS_SELECTOR, '.js_service_list > a:nth-child(4)').click()
        return SendMessagePage(self._driver)

    def contacts(self):
        self._driver.find_element(By.ID, 'menu_contacts').click()
        return ContactsPage(self._driver)

