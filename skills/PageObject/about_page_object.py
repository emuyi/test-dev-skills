"""
一、如何理解 PageObject：
    PageObject 是 ui自动化测试项目开发一种设计模式。简单理解 PageObject 实现了元素定位和元素操作的分层，
    主要是为了解决因界面 ui 变化而带来的繁重的用例维护问题。具体来讲，用例代码的组织应当像人操作界面UI
    一样只关心操作步骤，至于怎么去定位元素之类的逻辑应当由 page 层实现并且要提供良好的接口给测试用例。

    如 web 搜索测试：

        用例层：
            1. 打开网站
            2. 输入关键字
            3. 点击搜索按钮
            4. 断言

        page层：
            1. input 框的定位及相关的处理
            2. button 的定位
            并提供封装良好的接口给用例层(用例层不应当和 WebDriver API 有直接的接触)

    具体示例：base_page.py / bing_page.py / test_bing_search.py

二、Poium 是基于 Selenium/Appium Page Object 测试库，最大的特点就是简化了 Page 层元素的定义
    !!!! 源码写的很有意思哈，没事多看看，学学人家的设计思路。!!!!

    使用方式：
        from poium import Page, NewPageElement

        page 层：

            class BingPagePoium(Page):

                search_input = NewPageElement(id_='sb_form_q', timeout=2, describe='搜索框')
                search_button = NewPageElement(id_='sb_form_go', timeout=2, describe='搜索按钮')

        用例：

            class TestBingSearchPoium:

                def test_search(self, driver):
                    bpp = BingPagePoium(driver)
                    bpp.get('https://cn.bing.com/')
                    bpp.search_input = 'Page Object'
                    bpp.search_button.click()
                    time.sleep(0.5)
                    assert 'Page Object' in bpp.get_title

    相比我们自己的实现的 page object , poium 真正实现了元素定位和操作的分离，本质是用一个描述符对象来接管我们定义的search_input
    之类的属性。
"""
