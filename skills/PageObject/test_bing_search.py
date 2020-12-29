import pytest
import time
from bing_page import BingPage
from bing_page import BingPagePoium


class TestBingSearch:

    def test_search(self, driver):
        bp = BingPage(driver)
        bp.open('https://cn.bing.com/')
        bp.input('Page Object')
        bp.click()
        time.sleep(0.5)
        assert 'Page Object' in bp.title


class TestBingSearchPoium:
    """poium 版本"""
    def test_search(self, driver):
        bpp = BingPagePoium(driver)
        bpp.get('https://cn.bing.com/')
        bpp.input = 'Page Object'
        bpp.button.click()
        time.sleep(0.5)
        assert 'Page Object' in bpp.get_title

