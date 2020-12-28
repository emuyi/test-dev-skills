import pytest
import time
from selenium import webdriver

data = ['selenium', 'pytest', 'parameterized']


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





