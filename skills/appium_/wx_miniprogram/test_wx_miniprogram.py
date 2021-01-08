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

其他内容：
    5、小程序进程获取：
        打开小程序，命令行执行：adb shell dumpsys activity top | grep ACTIVITY
        --> 会出现：ACTIVITY com.tencent.mm/.plugin.appbrand.ui.AppBrandUI 2218aad pid=4312
        然后执行 adb shell ps 4312
        --> com.tencent.mm:appbrand0  即正在运行的小程序的进程

        desired_caps 中可以这样配置：
                desired_caps['chromeOptions'] = {
                'androidProcess': 'com.tencent.mm:appbrand0'
            }
    6、不方便科学上网可以使用 uc dev tools 也可以检视。
"""
import time

from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWxMiniProgram:
    def setup(self):
        caps = dict()
        caps["platformName"] = "Android"
        caps["deviceName"] = "phone"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
        caps["noReset"] = True
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True

        # caps['chromedriverExecutable'] = \
        #     '/Users/seveniruby/projects/chromedriver/chromedrivers/chromedriver_78.0.3904.11'

        caps['chromedriverExecutableDir'] = r'D:/android_chromedriver/'

        # options = ChromeOptions()
        # options.add_experimental_option('androidProcess', 'com.tencent.mm:appbrand0')
        caps['chromeOptions'] = {
            'androidProcess': 'com.tencent.mm:appbrand0'
        }

        # caps['adbPort'] = 5038 配合 proxy 使用

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        self.enter_mini_program()

    def enter_mini_program(self):
        time.sleep(3)
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.3, size['width'] * 0.5, size['height'] * 0.8)
        self.driver.find_element(By.XPATH, '//*[@text="哔哩哔哩"]').click()

    def test_search_webview(self):
        time.sleep(10)
        print(self.driver.contexts)
        # self.driver.switch_to.context(self.driver.contexts[-1])
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, "时尚的代价").click()

    def teardown(self):
        pass
        # self.driver.quit()


"""
    def find_top_window(self):
        for window in self.driver.window_handles:
            print(window)
            print(self.driver.title)
            if ":VISIBLE" in self.driver.title:
                print(self.driver.title)
            else:
                self.driver.switch_to.window(window)
"""