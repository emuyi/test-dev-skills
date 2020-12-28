"""
一. 最初的 selenium 是通过 js函数操作浏览器，2版本后使用 WebDriver 来控制浏览器，同时保证兼容 1版本的selenium
   3版本后的 selenium 去掉了 selenium RC(js操作浏览器)， 开始全面使用 WebDriver（通过原生浏览器支持或者浏览器扩展来直接控制浏览器）
   对浏览器进行操作。
二. selenium-ide ：提供了脚本录制和回放的功能，但最实用的是用它来帮忙导出元素定位语句。
三. WebDriver API 通俗来讲就是模拟鼠标和键盘对web页面进行操作，所以学习 WebDriver API，需要两步走：
第一步：定位元素
    selenium 提供了8种定位API
    driver.find_element_by_id()
    driver.find_element_by_name()  根据标签name属性
    driver.find_element_by_tag_name()
    driver.find_element_by_class_name()
    driver.find_element_by_link_text()  根据链接文本定位
    driver.find_element_by_partial_link_text() 根据连接文本中的部分信息定位
    driver.find_element_by_xpath()
    driver.find_element_by_css_selector() !!!!!!!

    另一种写法：driver.find_element(By.CSS_SELECTOR, '#kw')
    from selenium.webdriver.common.by import By
    其实 driver.find_element_by_css_selector('#kw') 内部返回的就是 driver.find_element(By.CSS_SELECTOR, '#kw')
第二步：操作元素
    1. 控制浏览器
        driver.get('https://www.baidu.com/') 打开网站
        driver.maximize_window() 窗口最大化
        driver.set_window_size(500, 500) # 像素
        driver.back() 后退
        driver.forward() 前进
        driver.refresh() 刷新浏览器
    2. 操作元素
        a. 常用的操作
            found_element.click()
            found_element.send_keys()
            found_element.clear() 清除表单中的数据
            found_element.submit() 提交表单
        b. 鼠标操作 ActionChains
            from selenium.webdriver import ActionChains

            ActionChains(driver).move_to_element(element) # move_to_element_with_offset/move_by_offset
            ActionChains(driver).click(element)
            ActionChains(driver).double_click(element)
            ActionChains(driver).context_click(element)
            ActionChains(driver).drag_and_drop(source_ele, target_ele)
            一定要记得用最后用 perform() 提交动作
        c. 键盘操作 Keys 支持常用的键盘按键和组合键
            from selenium.webdriver.common.keys import Keys
            send_keys('selenium')
            send_keys(Keys.ENTER) .....
            send_keys(Keys.CONTROL, 'c') ....
            send_keys(Keys.F1)......
    3. 查看元素属性
        found_element.size / found_element.text / found_element.get_attribute(name) / found_element.is_display() .....
四、常用的断言点
    可以通过比较前后web页面的 title， url，text等信息来作为断言点
    driver.title 网页标题
    driver.current_url 打开的网站url
    网页的上的文本信息，如搜索网站后经常会有的 ‘搜索的相关结果 xxx 条’ 之类的
-----------------------------------示例在：other_use.py---------------------------------------------
五、显示等待和隐式等待
    显示等待
        1、webdriver 等某个条件成立的时候的在执行，否则如果超出设置的超时时间，报 TimeoutException 异常。
            from selenium.webdriver.support.ui.WebDriverWait
            element = WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exception=NoSuchElementException)
            until(method, message='') 直到某个条件成立往下执行
            not until(method, message='') 直到某个条件不成立往下执行

            常和 expected_conditions 配合使用
            from selenium.webdriver.support import expected_conditions as EC
            比较常用的：
                EC.visibility_of_element_located((BY.ID, 'kw'))  判断元素是否可见（非隐藏且高宽不为0）
                EC.presence_of_element_located(locator) 判断元素是否被加载到 DOM 树中，但不一定是看见的
                EC.text_to_be_present_in_element_value(locator, str)
                其他的方法请看源码，写的很详细。

        2、以 until 为例阐述显示等待的原理

             end_time = time.time() + timeout
             where True:
                try:
                    ele = located_method()
                    return ele
                except NoSuchElement:
                    pass
                time.sleep(poll)
                if  time.time() > end_time:
                    break
             raise TimeoutException

    隐式等待
        1. driver.implicity_wait(5)
        2. 如何理解？
            隐式等待不是一个固定的时间，它面向的是整个driver的会话周期，即遇到要定位元素的语句的时候，
            如果能找到元素，程序会接着往下执行，否则的话，它会以轮询的方式去判断元素是否存在，
            如果轮询的时间超出了timeout时间，抛异常
        3. 显示等待的话更灵活且功能更丰富。
六、定位一组元素
    find_elements_by* 如：用 selenium 爬虫 爬所有的帖子的信息
七、switch_to 处理表单切换，多窗口切换，alert弹窗处理
    1. frame/iframe 表单切换(内嵌网页)
       driver.switch_to.frame(frameElement)
       driver.switch_to.default_content()
    2. 多窗口切换
       driver.switch_to.window(window_handle)
       driver.current_window_handle 当前的窗口的句柄
       driver.window_handles 以列表的形式返回所有窗口的句柄
       怎么切换呢？ for遍历抛去不是当前窗口的
    3. 切换到弹窗
       driver.switch_to.alert   # 做成了一个特性(看源码)，其实是一个Alert()
       有以下几个属性：
            text 弹窗文本
            accept() 接受现有的弹窗
            dismiss() 解散现有的弹窗
            send_keys() 向弹窗输入内容(如果能输入的话)
八、下拉框处理
    WebDriver 提供了专门的 Select 类来处理下拉框(select标签)
    from selenium.webdriver.support.select import Select

    Select(selectElement).select_by_value('10')  # 根据 value属性值定位
    Select(selectElement).select_by_visible_text('每页10条')  # 根据 text 值定位
    Select(selectElement).select_by_index(0) # 根据索引，第一个选项为 0，依次类推。

九、文件上传和下载
    文件上传：
        1. input标签实现的文件上传
            处理方式：直接找到input标签，然后给该标签 send_keys(文件地址)
        2. js，ajax，flash 实现的文件上传
            处理方式：借助autoIt或者win32gui实现上传和下载
    文件下载：
        主要是要针对不同的浏览器做不同的配置，比如文件下载的目录，禁止下载弹框之类
        options = webdriver.ChromeOptions()
        prefs = {
            'profile.default_content_settings.popups': 0,
            'download.default_directory': os.getcwd()
        }
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(options=options)
十、 WebDriver 操作 cookie
    查看：
        driver.get_all_cookies() [{},{},{}]
        driver.get_cookie('foo') 查看 name 是 foo 的 cookies记录
    添加cookie：
        driver.add_cookie(cookie_dict)  # name 和 value 是必须的
        cookie_dict: {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'foo', 'path': '/', 'secure': True, 'value': 'bar'}
    删除cookie：
        driver.delete_cookie('foo') 删除 name 是 foo 的 cookie
        driver.delete_all_cookies() 删除所有的 cookie
十一、调用 js
      WebDriver 不是万能的，比如不能滑动 web 窗口，这时可以配合 js 代码使用
     driver.execute_script(js_code)

十二、测试 HTML5 视频(video标签)
     通过调用js:
        # arguments 是一个对应于传递给函数的参数的类数组对象。这里的 arguments[0] == videoElement
        driver.execute_script('return arguments[0].currentSrc;', videoElement)  当前播放视频来源
        driver.execute_script('arguments[0].play();', videoElement)  播放
        driver.execute_script('arguments[0].pause();', videoElement) 暂停

        driver.execute_script('return arguments[0].currentTime;', videoElement) 当前视频播放时间
        driver.execute_script('return arguments[0].volume;', videoElement)  音量
        driver.execute_script('arguments[0].load();', videoElement)  加载
十三、滑动解锁&选择日期
    要用到 ActionChains 操作
    滑动解锁
        1.定位到 滑动块 元素
        2. ActionChain.click_and_hold().perform()
        3. ActionChain.move_by_offset(x,y).perform()
        4. 注意处理 UnexpectedAlertPresentException 异常
    选择日期
        1. 使用 ActionChains
        2. 使用 TouchActions (work like ActionChains)

十四、
    driver.save_screenshot() 保存截图
    driver.close() Closes the current window.

"""
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # 实例化 driver 对象
    yield driver
    driver.quit()

# 简单demo
# def test_baidu(driver):
#     driver.maximize_window()  # 最大化窗口
#     driver.get('https://www.baidu.com/')  #
#     # driver.set_window_size(500, 500)  # 设置浏览器窗口的大小
#     driver.find_element(By.CSS_SELECTOR, '#kw')
#     driver.get('https://news.baidu.com')
#     driver.back()  # 后退
#     time.sleep(1)
#     driver.forward()   # 前进
#     time.sleep(1)
#     driver.refresh()  # 刷新浏览器

# 操作元素
# def test_bilibili(driver):
#     driver.maximize_window()
#     driver.get('https://www.bilibili.com/')
#     # driver.find_element_by_css_selector('#nav_searchform input').send_keys('selenium')
#     # time.sleep(1)
#     # # driver.find_element_by_css_selector('#nav_searchform button').click()
#     driver.find_element_by_css_selector('#nav_searchform input').submit()  # 按 enter 回车提交表单
#     # time.sleep(1)
#     # driver.find_element_by_css_selector('#')
#
#     # 查看元素的信息
#     # input_ele = driver.find_element_by_css_selector('#nav_searchform input')
#     # print(input_ele.size)
#     # print(input_ele.text)
#     # print(input_ele.get_attribute('placeholder'))
#     # print(input_ele.is_displayed())
#     #
#     # 鼠标操作：ActionChains
#     # 移动鼠标 move_to_element(ele)
#     # 单击 click(ele)
#     # 双击 double_click(ele)
#     # 右击 context_click(ele)
#     # 拖拽 drag_and_drop(source_ele, target_ele)
#     # perform() 提交操作
#     ele_app = driver.find_element_by_css_selector('a[href="//app.bilibili.com"]')
#     # ActionChains(driver).move_to_element(ele_app).perform()
#     # ActionChains(driver).click(ele_app).perform()
#     # ActionChains(driver).double_click(ele_app).perform()
#     # ActionChains(driver).context_click(ele_app).perform()
#     time.sleep(1)
#     ele_upload = driver.find_element_by_css_selector('#primaryPageTab ul>li:nth-child(2)')
#     time.sleep(1)
#     ActionChains(driver).drag_and_drop(ele_app, ele_upload).perform()
#     time.sleep(5)
#     # 键盘操作
#     from selenium.webdriver.common.keys import Keys
#     # ele_app.send_keys('selenium')
#     # ele_app.send_keys(Keys.CONTROL, 'x')
#     # ele_app.send_keys(Keys.F1)


# 查看断言信息 可以通过比较 网页标题，文本信息，url信息来判断
def test_bilibili(driver):
    url = 'https://www.bilibili.com/'
    driver.get(url)
    assert '干杯' in driver.title
    assert driver.current_url == url


# 搜索框输入 selenium 测试返回页面是否正确
@pytest.fixture(params=['https://testerhome.com/'])   # 这里使用 mark 去做更合适，复用性更强
def open_website(request, driver):
    driver.maximize_window()
    driver.get(request.param)


def test_testerhome_search(driver, open_website):
    time.sleep(2)
    driver.find_element_by_css_selector('input[placeholder*=搜索]').send_keys('selenium')
    driver.find_element_by_css_selector('input[placeholder*=搜索]').submit()
    time.sleep(2)
    result_text = driver.find_element_by_css_selector('div.media-body').text
    # assert 'search?q=selenium' in driver.current_url
    assert 'selenium' in result_text








