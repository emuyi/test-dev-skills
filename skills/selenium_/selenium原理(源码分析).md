```python

简单来看 selenium 的工作流程：先起一个进程把浏览器驱动调起来，浏览器驱动会启动一个 server，然后 selenium 向这个 server 发送符合 webdriver 规范的指令请求，服务端收到请求后解析，然后根据请求操作浏览器并把结果返回。


具体源码分析如下：

# 源码流程分析(以 chrome 为例)
打开浏览器：
    driver = webdriver.Chrome()
        1. 执行 service.start 方法 通过 subprocess.Popen 启动浏览器驱动(chrome driver)
        2. 调用父类 RemoteWebDriver 的 init 方法，初始化 RemoteConnection 对象并且调用
           start_session 方法，该方法调用 execute 方法执行了一个 NEW_SESSION 的command
        3. 而这个 execute 方法实质上是调用 urllib3 的 request 方法向 http://localhost:xxxx/session
           发送了一个 post 请求，即向浏览器驱动发送了一个打开浏览器的请求，chrome driver 启动浏览器并返回
           sessionid

操控浏览器：
    driver.get('http://xxx.com') (这里以driver.get为例)
        调用 RemoteWebDriver 的 execute 方法去执行打开某个网站的command，而实际上该方法调用了 RemoteConnection
        的 execute 方法，这个方法会 去self._command 一个私有属性里去查找你发送命令的对应的请求方式和请求uri，比如 get指令
        对应的请求方式是 post，请求 uri 是/session/$sessionId/url ，然后 selenium 会将 uri 拼接成 
        http://localhost:xxxx/session/$sessionId/url 然后使用 urllib3 的 request 方式像这个 url 发送 post 请求。
        即向浏览器驱动程序发送了一个打开网站的请求。本质上和上面的 start_session 的流程是一样的。
      

# 如何理解 webdriver 协议以及 json wire protocol
    本质上来讲：webdirver 协议规定了 command，请求方式，请求uri之间的一种映射关系。
    如 newSession command 对应 post 的请求方式，请求uri是 /session
    如 get 打开某个网址的 command，对应 post的请求方式，请求 uri 是 /url
    如 find_element, comand，对应 post的请求方式，请求 uri 是 /element

# 关于 json wire protocol
     json wire protocol 其实是在 http 协议上对请求以及响应上做了一些其他的规范
     比如说在相应上增加了一些其他的相应状态
            7： NoSuchElement
            
            11：ElementNotVisible
            
            200：Everything OK
     最重要的是在请求体数据上它是以 json 的格式来构造数据，这也是它为什么支持多种语言的原因。

    
    












```

