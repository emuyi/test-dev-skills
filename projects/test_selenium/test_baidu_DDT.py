import unittest
import time
from ddt import ddt, data, unpack
from selenium import webdriver


@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = 'https://www.baidu.com/'

    def baidu_search(self, search_key):
        self.driver.get(self.url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        return self.driver.title

    @data(['case1', 'selenium'], ['case2', 'unittest'], ['case3', 'ddt'])
    @unpack
    def test_baidu_search(self, case, search_key):
        print('run {} search key:{}'.format(case, search_key))
        result = self.baidu_search(search_key)
        self.assertIn(search_key, result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
