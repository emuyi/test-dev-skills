"""
工作原理：
    1、Appium 的工作原理和 selenium 很类似，不过是将 WebDriver 换成了 Appium Server，同样是
    测试脚本(client) 向 Appium Server 发送请求，Server 接受到请求后解析请求并操作移动设备或者模拟器
    然后将操作结果 response。
    2、appium  API 是在支持 selenium API 基础上又进行了扩展，如 appium 的 command 直接是对 webdriver 的 Remote
    Connection._commands 这个属性字典进行赋值扩展处理。

基本用法：
    一、环境
         server端: appium-desktop（appium server 的图形化工具，类似 selenium-ide）
            ！注意 server 端出现 No Android home 等环境变量问题时，可以去appium-desktop config 里面设置下
         client端：就 python 而言，appium-python-client 包

    二、使用
    from appium import webdriver

    # 配置信息【!!注意配置项是优化appium性能的一个主要点,下面的链接要经常看】
    # 参考：https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
    desired_caps = {
        'deviceName': 'Android Emulator',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '11',
        'appPackage': 'com.google.android.apps.nexuslauncher',
        'appActivity': 'com.google.android.apps.nexuslauncher.NexusLauncherActivity',
        'noReset': True,   # 不重置应用
        'udid':'emulator-5554' # 指定执行的设备
        'unicodeKeyboard':true # 支持输入中文
        'restKeyboard': true # 重置输入法
        'dontStopAppOnReset': true  # 如果为 true 类似于 am start -S 先停止应用在启动应用
        'skipServerInstallation': true # 如果设备上已经有合适版本的uiautomator2那就不再安装 uiautomator2
        'chromedriverExecutableDir': /xx/xx/ 指定不同版本的 chromedriver 放在一个目录下，appium server 会自动寻找
        'chromedriverExecutable': 指定特定版本的chromedriver

    }
    ! 注意可以使用 adb shell dumpsys activity | grep(findstr) mCurrentFocus 或
    adb shell dumpsys window | grep(findstr) mCurrentFocus 来获取 appPackage 及 appActivity

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub')   # 4723： appium server 默认端口号
    driver.find_element_by_id('xxxxx').click()
    driver.quit()

常用 API：
    一、定位控件
        driver.find_element_by_id()    # resource-id 属性
        driver.find_element_by_xpath()
        driver.find_element_by_accessibility_id()   # Android 里相当于 content-desc 属性

        # 根据 uiautomator2 语法来定位 【速度快，但仅限Android】
        # new UiSelector().text("Camera"); .description(); .resourceId();
        driver.find_element_by_android_uiautomator('new UiSelector().text("Camera")')
        driver.find_element_by_class_name()  # class 属性


        至于 webdriver 的 find_element_by_name/ by_tag_name/ by_link_text 之类的在 web app 或者混合应用的 WebView（原生 app 中内嵌 web
        网页）中可以使用

        其他的API:
            driver.find_element_by_ios_predicate()
            driver.find_element_by_ios_uiautomation()
            driver.find_element_by_ios_class_chain()

    二、常用操作
         101！！！ 请务必多翻下 https://appium.io/docs/en/about-appium/intro/ 的 Commands 标签， 介绍的非常全。
        1、 操作应用
            driver.install_app(xx.apk)
            driver.remove_app(packageName)

            driver.close_app()  # 关闭应用
            driver.launch_app()  # 启动应用 常和 close_app() 配合使用，因为默认情况下实例化driver的时候配置的应用就会被启动

            driver.is_app_installed(packageName)
            driver.background_app(5)  # 将应用置于后台5s
            driver.reset()  # 重置应用，相当于清除应用缓存
            driver.current_package/driver.current_activity

        2、 上下文操作 （针对混合应用）
            WebView 组件无法通过 uiautomatorviewer 进行定位，且属性一般包含 WebView
            contexts = driver.contexts   # ['NATIVE_APP', 'WEBVIEW_xxx']
            driver.switch_to.context('WEBVIEW_xxx')
            current_context = driver.current_context
            driver.switch_to.context('NATIVE_APP')

        3、键盘操作（注意光标要聚焦到输入框）
            driver.find_element_by_id('android:id/search_src_text').send_keys('display')
            driver.keyevent(keycode) # http://developer.android.com/reference/android/view/KeyEvent.html
            driver.hide_keyboard()  收起虚拟键盘

        4、TouchAction （tap，long_press, move_to, wait).perform()

            from appium.webdriver.common.touch_action import TouchAction
            action = TouchAction(driver)

            action.tap(widget=None, x=None, y=None).perform()
            action.long_press(widget=None, x=None, y=None).perform()

            # press 和 move 配合链式操作，实现移动控件以及多点触控的效果 !!!!
            action \
            .press(x=start_x, y=start_y) \
            .wait(ms=duration) \  等价于 driver.swipe(startX, startY, endX, endY)
            .move_to(x=end_x, y=end_y) \
            .release()
             action.perform()
        5. 其他操作
            width, height = driver.get_window_size()
            driver.lock(5) 锁屏并息屏5s, 5s后自动解锁亮屏，和按锁屏键效果一样
            driver.push_file(devicePath, localPath)       感觉不如 adb push 和 adb pull 好用
            file_content = driver.pull_file(deviceFilePath)


        6. execute_script() 去执行 adb 相关的命令
            前提是 appium server 启动的时候要加上 --relaxed-security 参数

             result = self.driver.execute_script('mobile:shell', {
                'command': 'ps',
                'args': ['-e', '-f'],
                'includeStderr': True,
                'timeout': 5000
            })
            print(result.get('stdout'))

    三、断言
        element.text 文本来做断言
        根据定位到的 element.get_attribute() 来做断言
        如：resource-id, content-desc, text, class 等 uiautomatorviwer 中显示的都可以获取

"""

