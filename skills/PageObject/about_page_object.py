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


二、补充 Page 设计的原则【根据实际来，PO本质上其实就是对业务的高度抽象】

    The public methods represent the services that the page offers     # Page 关注的是一个页面提供的功能而不是操作细节
    Try not to expose the internals of the page                        # Page 应当隐藏定位细节
    Generally don't make assertions                                    # Page 中不应当出现断言
    Methods return other PageObjects                                   # 如首页上会提供很多的快捷入口，那么测试 index_page的时候，可以直接返回对应的入口的PO
    Need not represent an entire page                                  # 没必要给整个页面建模
    Different results for the same action are modelled as different methods     # 同一个功能，但结果不同，应当分成两个方法

   具体示例：simple_po 请尽量根据 simple_po 模式来设计 !!!!!!!


三、Poium 是基于 Selenium/Appium Page Object 测试库，最大的特点就是简化了 Page 层元素的定义

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
"""
