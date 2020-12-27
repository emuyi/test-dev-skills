import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# 显示等待
def test_baidu_search(driver):
    driver.maximize_window()
    driver.get('https://www.baidu.com/')
    # ele_search = WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.ID, 'kw11')))
    ele_search = driver.find_element_by_id('kw')
    ele_search = WebDriverWait(driver, 5).until(EC.visibility_of(ele_search))
    ele_search.send_keys('selenium')
    time.sleep(1)
    ele_search.submit()
    assert 1


# 隐式等待
def test_baidu_search_implicitly(driver):
    driver.implicitly_wait(2)
    driver.get('https://www.baidu.com/')
    driver.find_element_by_css_selector('#kw').send_keys('selenium')
    driver.find_element_by_css_selector('#kw').submit()
    ret = driver.find_element_by_css_selector('.nums_text').text
    assert '百度为您找到相关结果' in ret


# 定位一组元素
def test_baidu_search_results(driver):
    driver.implicitly_wait(2)
    driver.get('https://www.baidu.com/')
    time.sleep(4)
    driver.find_element_by_css_selector('#kw').send_keys('selenium')
    driver.find_element_by_css_selector('#kw').submit()
    ret = driver.find_element_by_css_selector('.nums_text').text
    if '百度为您找到相关结果' in ret:
        rets = driver.find_elements_by_css_selector('h3.t>a')
        for item in rets:
            print(item.text, item.get_attribute('href'))
    assert 1


# frame/iframe 切换（内嵌网页）driver.switch_to.frame()
def test_switch_to_frame(driver):
    driver.implicitly_wait(2)
    driver.get('https://www.126.com/')
    login_frame = driver.find_element_by_css_selector('iframe[id^=x-URS-iframe]')
    driver.switch_to.frame(login_frame)  # 切换到frame
    driver.find_element_by_name('email').send_keys('112312312')
    driver.find_element_by_name('password').send_keys('sfsdfasdfs')
    driver.find_element_by_id('dologin').click()
    driver.switch_to.default_content()  # 切换回来
    # error_info = driver.find_element_by_css_selector('#nerror>div.ferrorhead').text
    # assert '错误' in error_info
    assert 1


# 多窗口切换(根据窗口句柄切换,for 遍历句柄列表找不是当前做切换)
def test_switch_to_window(driver):
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://www.baidu.com/')
    index_window_handle = driver.current_window_handle
    driver.find_element_by_link_text('登录').click()
    driver.find_element_by_link_text('立即注册').click()
    for window_handle in driver.window_handles:
        if window_handle != index_window_handle:
            driver.switch_to.window(window_handle)
    driver.find_element_by_id('login_btn').click()
    assert 1


# 弹窗处理（alert, confirm, prompt)
def test_switch_to_alert(driver):
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get('https://www.baidu.com/')
    ele_setting = driver.find_element_by_id('s-usersetting-top')
    ActionChains(driver).move_to_element(ele_setting).perform()
    time.sleep(5)
    driver.find_element_by_link_text('搜索设置').click()
    driver.find_element_by_link_text('保存设置').click()
    alert = driver.switch_to.alert  # driver.switch_to.alert
    print(alert.text)
    time.sleep(1)
    # alert.accept()
    alert.dismiss()
    #  alert.send_keys()
    time.sleep(5)
    assert 1


# 处理下拉框 Select 类
def test_select(driver):
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get('https://www.baidu.com/default.html')
    driver.find_element_by_link_text('搜索设置').click()
    ele_select = driver.find_element_by_id('nr')
    Select(ele_select).select_by_value('20')
    time.sleep(1)
    Select(ele_select).select_by_visible_text('每页显示50条')
    time.sleep(1)
    Select(ele_select).select_by_index(0)
    time.sleep(1)
    assert 1


# 处理文件的上传和下载
# 1. input 实现的 send_keys(文件路径) 2. js，ajax，flash 实现的上传，使用autoIt，.win32gui
def test_file_upload(driver):
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get('http://www.sahitest.com/demo/php/fileUpload.htm')
    driver.find_element_by_id('file').send_keys("D:\\a.png")
    driver.find_element_by_css_selector('form[name=form1]>input[name=submit]').click()
    time.sleep(5)






