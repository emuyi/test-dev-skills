"""
selenium grid 分布式执行用例， 分为 hub 和多个 node，hub 主要是用来管理 node 的注册以及状态，并且可以根据用例的配置信息
来自动转发用例到匹配的 node 上。

(首先要下载 selenium-server)
启动 hub:  java -jar selenium-server-standalone-3.141.59.jar -role hub  (hub 默认端口：4444)
启动 node: java -jar selenium-server-standalone-3.141.59.jar -role node -port 5555 -hub http://192.168.0.0:4444/grid/register/
(可以通过 http://192.168.0.0:4444/grid/console/ 在浏览器中查看 node 信息)
如果要启动远程 node，需要满足以下几个条件：1.hub主机和远程node主机必须能互相ping通，2.远程node上要装selenium-server以及相应的浏览器驱动

selenium grid 使用如下：
"""

from selenium.webdriver import Remote, DesiredCapabilities

driver = Remote(desired_capabilities=DesiredCapabilities.CHROME.copy())
driver.get('https://cn.bing.com/')
driver.quit()

"""
上述代码执行流程： 测试用例将发起打开浏览器的请求，hub 接收到请求后解析用例的 desired_capabilities【包含浏览器的类型，版本，测试平台等信息】参数
根据这些参数将请求发送给匹配参数信息的 node 上，由 node 调用本机上的 webdriver 来操控浏览器。

"""

