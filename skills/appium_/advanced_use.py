"""
记录 appium 一些比较高级的用法
"""
"""
1、从源码编译 appium server (a.cnpm 安装的 appium 有问题 b. 可以体验appium最新的特性甚至是对源码做二次封装)
环境准备：
    a、安装 node.js
    b、配置 cnpm  参考：https://github.com/cnpm/cnpm [配置完成后注意添加下环境变量]
    c、从源码编译 appium server  参考：https://appium.io/docs/en/contributing-to-appium/appium-from-source/#running-appium-from-source
        
        git clone https://github.com/appium/appium.git
        cd appium
        cnpm install
        npm run build
        node .
2、appium shell client 
    appium 的本质就是向 http://127.0.0.1:4723/wd/hub/ 发送符合 webdriver 协议的请求，所以，也可以用 shell 来执行相关命令
    
# 基于 curl 命令向 appium server 发送符合 webdriver 协议的请求
# newSession command 并返回sessionId
 new_session(){
	session_id=$(curl -X POST -s http://127.0.0.1:4723/wd/hub/session \
	-d '{"capabilities":{"firstMatch":[{"appium:deviceName":"android emulator","appium:automationName":"uiautomator2","platformName":"android","appium:platformVersion":"11","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.view.WelcomeActivityAlias","appium:chromedriverExecutableDir":"D:/android-chromedriver/","appium:noReset":true,"appium:skipDeviceInitialization":true,"appium:skipServerInstallation":true}]},"desiredCapabilities":{"deviceName":"android emulator","automationName":"uiautomator2","platformName":"android","platformVersion":"11","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.view.WelcomeActivityAlias","chromedriverExecutableDir":"D:/android-chromedriver/","noReset":true,"skipDeviceInitialization":true,"skipServerInstallation":true}}' \
	-H "Content-Type:application/json;charset=UTF-8" | jq -r .value.sessionId)  
	# -r:raw，即直接将结果字符串直接输出，而不再输出json字符串
 }
 
# find element
find_element(){
	element_id=$(curl -X POST -s http://127.0.0.1:4723/wd/hub/session/$session_id/element \
	-d '{"using": "xpath", "value":"//*[@text=\"行情\"]"}' \
    -H "Content-Type:application/json;charset=UTF-8"  | jq -r .value.ELEMENT)
}

# click
click(){
	curl -X POST -s http://127.0.0.1:4723/wd/hub/session/$session_id/element/$element_id/click \
	-d '{"id":"${element_id}"}' \
	-H "Content-Type:application/json;charset=UTF-8"
}

3、如果要想要提速 appium 的元素定位以及定制某些操作功能，那就需要对 uiautomator-server 进行二次封装
源代码地址：https://github.com/appium/appium-uiautomator2-server 【java】

4、关于微信小程序测试：
    首先就目前来讲，对于小程序测试没有一个比较好的成熟的解决方案。主要可以通过以下三种方式进行测试：
    1、使用微信官方提供的自动化测试框架 minium，但该框架开发的目的只是为了方便小程序开发者调试，不能完全满足自动测试的需求
    2、appium + webview的方式，
        首先新版本的微信已经将 x5debug 调试小程序的功能给禁用了，模拟器就不能用
        如果是真机的话，需要root+工具强制将 webview 调试的功能打开，但这个也有问题，分手机类型
    3、native 定位 + PO，原生定位难免会出现定位符不准的问题，虽然通过 PO 的方式可以多多少少减轻一些用例维护的成本，但还是不太好用。
"""