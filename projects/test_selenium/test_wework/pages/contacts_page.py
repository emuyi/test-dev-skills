"""
通讯录页面
"""
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class ContactsPage(BasePage):
    """定义通讯录页面功能，暂时仅提供显示通讯录信息的功能"""

    @property
    def member_info(self):
        info_elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td > span')
        return '|'.join([info_ele.text for info_ele in info_elements])