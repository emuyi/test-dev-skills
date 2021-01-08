"""
1、关于微信小程序：https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/ 简单理解微信小程序，
  是对 webview 的定制封装，因此测试的关键还是如何顺利的切换到 webview 界面，并确保 chromedriver和小程序之间比较流畅度的通信。
2、微信官方提供的小程序自动化测试工具：
    https://developers.weixin.qq.com/miniprogram/dev/devtools/auto/quick-start.html
    https://cloud.tencent.com/developer/article/1647105
3、如何使用 appium 对小程序进行自动化测试
    a、需要打开微信 x5 内核调试开关
       在微信中打开 http://debugx5.qq.com
       选项卡中设置 inspect 调试之类的，能不能在 google 的 devtools 中检视的到，这个看运气，有的手机
       不用设置，有的手机设置了也没用！【强烈吐槽】
        没有 x5 内核 微信中打开 http://debugtbs.qq.com，安装 x5 内核
    b、在 devtools 中 inspect 小程序 webview，前提是 a 能成功。
    c、 devtools 中能显示小程序是用的 webview 版本，下载对应的 chrome 版本 https://npm.taobao.org/mirrors/chromedriver/
    d、设置配置项除了要指定 chromedriverExecutableDir 之类的外，还要注意配置 androidProcess': 'com.tencent.mm:appbrand0'
       因为小程序和微信不是同一个进程。

4、其他的就基本和 webview 测试一样了。

"""
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWxMiniProgram:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "测试人社区 ceshiren.com"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
        caps["noReset"] = True
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True

        caps['chromedriverExecutable'] = \
            '/Users/seveniruby/projects/chromedriver/chromedrivers/chromedriver_78.0.3904.11'

        # options = ChromeOptions()
        # options.add_experimental_option('androidProcess', 'com.tencent.mm:appbrand0')
        caps['chromeOptions'] = {
            'androidProcess': 'com.tencent.mm:appbrand0'
        }

        caps['adbPort'] = 5038

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(10)

        self.enter_micro_program()
        print(self.driver.contexts)

    def enter_micro_program(self):
        # 原生自动化测试
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width'] * 0.5, size['height'] * 0.9)
        self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
        self.driver.find_element(By.XPATH, "//*[@text='取消']")
        self.driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys("雪球")
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
        self.driver.find_element(By.XPATH, "//*[@text='自选']")

    def find_top_window(self):
        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                print(self.driver.title)
            else:
                self.driver.switch_to.window(window)

    def test_search_webview(self):
        # 进入webview
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.implicitly_wait(10)
        self.find_top_window()

        # css定位
        self.driver.find_element(By.CSS_SELECTOR, "[src*=stock_add]").click()
        # 等待新窗口
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR, "._input").click()
        # 输入
        self.driver.switch_to.context("NATIVE_APP")
        ActionChains(self.driver).send_keys("alibaba").perform()
        # 点击
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item")
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item").click()