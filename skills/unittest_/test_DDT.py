"""
ddt 配合 unittest 做数据驱动测试
主要用到 ddt.ddt, ddt.data, ddt.unpack, ddt.file_data 四个装饰器
@ddt：修饰整个测试类
@data: 存放参数， 参数的组织形式可以是列表，元祖，字典；当有多个参数 注意使用 @unpack进行拆包
@file_data(xx.json/xx.yml) 支持从 json 或者 yaml 文件中直接导出数据
"""
import unittest
import time
from ddt import ddt, data, unpack, file_data
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

    # @data(['case1', 'selenium'], ['case2', 'unittest'], ['case3', 'ddt'])  # 或者是用元祖组织的数据
    # @unpack
    # def test_baidu_search(self, case, search_key):
    #     print('run {} search key:{}'.format(case, search_key))
    #     result = self.baidu_search(search_key)
    #     self.assertIn(search_key, result)

    # @data({'search_key': 'selenium'}, {'search_key': 'selenium'})
    # @unpack
    # def test_baidu_search(self, search_key):
    #     result = self.baidu_search(search_key)
    #     self.assertIn(search_key, result)

    # @file_data('data.yml')
    # @unpack   # 多个对象需要 unpack
    # def test_baidu_search(self, **kwargs):
    #     search_key = kwargs.get('search_key')
    #     result = self.baidu_search(search_key)
    #     self.assertIn(search_key, result)

    @file_data('data.json')
    def test_baidu_search(self, **case):
        xx = case.get('xx')
        result = self.baidu_search(xx)
        self.assertIn(xx, result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
