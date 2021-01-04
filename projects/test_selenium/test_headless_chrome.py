import time
from selenium import webdriver


class TestTesterHome:

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        # todo 开启 debugger 模式
        # options.debugger_address = '127.0.0.1:9222'
        # todo headless chrome
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get('https://testerhome.com/')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_search_article(self):
        self.driver.find_element_by_link_text('tep 用户手册帮你从 unittest 过渡到 pytest').click()
        self.driver.find_element_by_css_selector('button[data-toggle=dropdown]').click()
        self.driver.find_element_by_css_selector('.list li:nth-child(10) > a').click()

    @classmethod
    def teardown_class(cls):
        time.sleep(5)
        cls.driver.quit()