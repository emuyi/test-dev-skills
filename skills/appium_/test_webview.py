"""
1、Native APP: 原生APP，Android 使用 java 开发，ios使用oc或者swift开发的应用
2、web app：网站的手机版，即常说的m站
3、hybrid app：混合应用，即 Native框架内嵌web内容 hybrid app允许开发者仅使用一套前端代码（HTML5+CSS+JavaScript），
   即可开发能部署在不同平台上的应用 。由于hybrid app结合了native app良好用户交互体验和web app跨平台开发的优势，
   能够显著节省移动应用开发的时间和成本。https://zhuanlan.zhihu.com/p/21387961

   内嵌 web 网页往往是由 WebView 组件来实现，webview 是一个基于webkit引擎展现web页面的控件。 如 android.webkit.WebView
   最直接的判断方式是使用 uiautomatorviewer 渲染不出来控件内容，也说明该控件可能是一个 WebView 组件

4、 测试 WebView 有两种方式
    1）不推荐。使用 uiautomatorviewer 其实会渲染 webview 组件，只需要刷新下 app就可以。然后 uiautomatorviewer 会使用 android.
    view.View 作为 webview控件的类，其中 webview中元素的innerText属性会被映射为 text属性（Android 11）注意不同版本，映射的属性值
    不一样，如Android 6 会被映射成 content-desc 属性。并且使用这种原生定位的方式问题会比较多，不要使用，了解即可。

    2）通过 switch_to.context(WBEVIEW_xxx) 定位

    101！！！环境准备：https://aotu.io/notes/2017/02/24/Mobile-debug/index.html

    模拟器（原生/genymotion)
        a. Android 4+ 的版本可以直接访问，chrome://inspect#device ， 在 chrome DevTools 里直接进行调试
           注意！ 如果使用 devtool 调起来有bug，可以尝试将 chrome 版本回退至 62
        b. 在 devtool 里点击 inspect 的时候需要科学上网
        c. 指定好对应 view 版本的 chromedriver [Found Chrome bundle 'com.google.android.webview' version ]
    真机环境：
        必须在 APP 内启动 WebView 调试。
        要启动 WebView 调试，需要调用 WebView 类上的静态方法 setWebContentsDebuggingEnabled。
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
        WebView.setWebContentsDebuggingEnabled(true);
        }
"""
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = dict(
    deviceName='android emulator',
    automationName='uiautomator2',
    platformName='android',
    platformVersion='11',
    appPackage='com.xueqiu.android',
    appActivity='com.xueqiu.android.view.WelcomeActivityAlias',
    chromedriverExecutableDir=r'D:/android-chromedriver/',
    noReset=True,
    skipDeviceInitialization=True,
    skipServerInstallation=True

)


class TestWebView:

    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)

    def test_webview(self):
        trade = (By.XPATH, '//*[@text="交易" and contains(@resource-id, "tab")]')
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(trade))
        self.driver.find_element(*trade).click()
        print(self.driver.contexts)  # ['NATIVE_APP', 'WEBVIEW_com.xueqiu.android']
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.window_handles)  # 3个窗口
        self.driver.find_element(By.CSS_SELECTOR, "div[class^='trade_home_info']").click()
        # 注意这块有可能是一个 trick，它实际上是新打开了一个窗口 所以当定位没问题，死活定位不到元素时，就要考虑是否新打开了窗口
        print(self.driver.window_handles)  # 4个窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.CSS_SELECTOR, '#phone-number')
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(phone))
        self.driver.find_element(*phone).send_keys('12345678910')

    def test_execute_script(self):
        result = self.driver.execute_script('mobile:shell', {
            'command': 'ps',
            'args': ['-e', '-f'],
            'includeStderr': True,
            'timeout': 5000
        })
        print(result.get('stdout'))

    def teardown(self):
        self.driver.quit()
