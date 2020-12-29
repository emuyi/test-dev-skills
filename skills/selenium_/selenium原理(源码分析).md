```python

通俗来看 selenium 的工作流程：先起一个进程把浏览器驱动调起来，然后把浏览器驱动程序当做一个 server，向这个 server 发送
一个 post 请求，让浏览器驱动把浏览器打开，后续一系列操作浏览器的行为都是向浏览器驱动程序发送对应的请求，然后浏览器驱动根据
请求去操控浏览器并把结果 response 回来。

具体源码分析如下：

# 源码流程分析(以 chrome 为例)
打开浏览器：
    driver = webdriver.Chrome()
        1. 执行 service.start 方法 通过 subprocess.Popen 启动浏览器驱动(chrome driver)
        2. 调用父类 RemoteWebDriver 的 init 方法，初始化 RemoteConnection 对象并且调用
           start_session 方法，该方法调用 execute 方法执行了一个 NEW_SESSION 的command
        3. 而这个 execute 方法实质上是调用 urllib3 的 request 方法向http://localhost:9515/session
           发送了一个post请求，即向浏览器驱动发送了一个打开浏览器的请求，chrome driver 启动浏览器并返回
           sessionid

操控浏览器：
    driver.get('http://xxx.com') (这里以driver.get为例)
        调用 RemoteWebDriver 的 execute 方法去执行打开某个网站的command，而实际上该方法调用了 RemoteConnection
        的 execute 方法，这个方法会 去self._command 一个私有属性里去查找你发送命令的对应的请求方式和请求uri，比如 get指令
        对应的请求方式是 post，请求 uri 是/session/$sessionId/url ，然后 selenium 会将 uri 拼接成 
        http://localhost:9515/session/$sessionId/url 然后使用 urllib3 的 request 方式像这个 url 发送 post 请求。
        即向浏览器驱动程序发送了一个打开网站的请求。本质上和上面的 start_session 的流程是一样的。
      
```

