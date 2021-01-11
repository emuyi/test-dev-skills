"""app 首页"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.profile_page import ProfilePage
from pages.search_page import SearchPage
from pages.trade_page import TradePage


class MainPage(BasePage):

    def goto_search(self):
        """跳转到搜索页面"""
        self.find(By.ID, 'tv_search').click()
        return SearchPage(self._driver)

    def goto_trade(self):
        """跳转到交易页面"""
        self.find(By.XPATH, '//*[@text="交易" and contains(@resource-id, "tab")]').click()
        return TradePage(self._driver)

    def goto_profile(self):
        """跳转到我的页面"""
        self.find_by_text('我的').click()
        return ProfilePage(self._driver)




























