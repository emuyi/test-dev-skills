
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.contacts_page import ContactsPage


class ImportContactPage(BasePage):
    """定义批量导入页面功能"""

    def upload_contact_file(self, file_path):
        self._driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')\
            .send_keys(file_path)
        self._driver.find_element(By.LINK_TEXT, '导入').click()
        locator = (By.LINK_TEXT, '完成')
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(locator))
        self._driver.find_element(*locator).click()
        return ContactsPage(self._driver)
