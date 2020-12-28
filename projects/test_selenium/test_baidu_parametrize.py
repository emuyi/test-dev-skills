"""
不能把 parameterized 简单的理解成把测试用例的数据做参数然后传给它，因为传参的形式测的是一个用例
但传参的目的是要测试多种情况，理应是多个测试用例。
参数化的百度搜索
"""
import pytest
import time
from selenium import webdriver

data = ['selenium', 'pytest', 'parameterized']


# !!!!!!!!!!!!!!!! 如果这里不加 scope 会怎么样？
@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def baidu_search(request, driver):
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys(request.param)
    driver.find_element_by_id('su').click()
    time.sleep(2)
    return request.param, driver.title


class TestBaidu:
    @pytest.mark.parametrize('baidu_search', data, indirect=True)
    def test_search(self, baidu_search):
        expected, result = baidu_search
        assert expected in result





