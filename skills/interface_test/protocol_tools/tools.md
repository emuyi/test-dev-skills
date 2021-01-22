#### 网络分析工具

##### 1、tcpdump

```bash
tcpdump 可以根据一定的过滤机制来抓取想要的数据包，常使用 -w 将数据写入文件再通过 wireshark 进行分析。
常用参数：
	host：过滤器，即只获取host指定ip的数据。tcpdump host www.baidu.com 
	port：过滤器，只获取指定端口的数据
	src：过滤器，常和host搭配使用。tcpdump src host www.baidu.com(只获取从百度过来的数据)	
	dst：过滤器，同src，和host搭配使用。tcpdump dst host www.baidu.com (只获取发给百度的数据)
	and or not：逻辑运算，通常用来连接多个过滤规则 tcpdump host www.baidu.com and port 80
	-w：将抓取到的数据写入到文件
	-v：数据的详细程度，分为 -v，-vv，-vvv
	-A：以ASCII的形式输出数据包，适合用来捕获web请求
	-l：对标准输出进行行缓冲
	-c：指定抓取多少个包，不指定会一直抓取直到强制退出
	使用tcpdump命令需要root权限
更多参数参考：
	http://www.tcpdump.org/manpages/tcpdump.1.html(首推)
	https://www.cnblogs.com/ggjucheng/archive/2012/01/14/2322659.html
	https://zhuanlan.zhihu.com/p/182802540
```

##### 2、wireshark

```shell
相比tcpdump wireshark图形化界面能更好的帮助抓包后的分析，并且使用wireshark不仅可以抓取http/https的数据包，也能抓取 tcp/udp 比较偏底层协议的数据包。
如果要用wireshark请参考：https://www.cnblogs.com/zhaopei/p/12152139.html
```

#### HTTP/HTTPS 抓包工具

##### 1、charles

```shell
charles 本质上是将自己做为系统网络的代理服务器，所有的网络请求和响应都要经过它，因此可以实现
网络数据的截取和分析。
比较有用的功能：
	2、模拟弱网
    	Proxy --> Throttle Settings 
    3、在指定的端口设置代理
    	Proxy --> Proxy Settings
    4、抓取https请求
    	web：https://blog.csdn.net/u011019468/article/details/107404990
    	安卓模拟器：6.0以下的版本接受用户级别的证书，以上的版本需要修改apk包的属性
    			  1.手机上设置代理，charles代理可以通过 help->ssl proxy->install * on mobile device 会弹框提示
    			  	代理的ip的端口，一般情况下就是主机ip，端口也可以在Proxy --> Proxy Settings
    			  	【模拟器右侧工具栏 ... --> setting --> proxy】
    			  2. 手机浏览器访问 http://chls.pro/ssl 下载并安装证书
    	安卓模拟器搞不了，用雷电模拟器，低版本的夜神理论上也可以。
	5、mock
		tools--> rewrite(最常用)-->enable rewrite
		tools--> map remote
		tools--> map local
	1、指定要录制(抓取)的网站
		Proxy --> Recording Settings --> Include		
https://www.charlesproxy.com/documentation/(首推)
https://juejin.cn/post/6844903665304600589
```

##### 2、chrome Network 面板

```shell
深入了解参考：https://developers.google.com/web/tools/chrome-devtools/network/?utm_source=devtools&utm_campaign=2019Q1
# 比较实用的一个功能 copy as curl https://blog.csdn.net/u011519550/article/details/106130050
```

##### 3、fiddler

```shell
fiddler 提供的功能和charles类似
如果要用fiddler请参考：https://www.jianshu.com/p/99b6b4cd273c
```

#### 请求工具

##### 1、curl

```shell
-o 将响应信息保存为文件，curl -L -s -o 'ret.html'  http://www.taobao.com
-A 指定User-Agent，注意尽量用单引号。 curl -A 'emuyi' www.taobao.com
-b 携带cookie, curl -b 'foo=bar;a=1' www.baidu.com 或从文件中读取cookie，和-c配合使用
-c 将服务器设置的cookie写入到文件 curl -b cookies.txt www.baidu.com -v
-d 指定post请求发送的数据，默认数据类型是*urlencoded的，并且会自动将请求转换为post， -X POST可以忽略。
$ curl -d'login=emma＆password=123' https://google.com/login
# 或者
$ curl -d 'login=emma' -d 'password=123' https://google.com/login
curl -d @data.txt https://google.com/login
--data-urlencode 类似-d 区别在于会自动将发送的数据进行 URL 编码长和 -G 配合使用
-e 设置请求头，请求的来源 即referer
-F 向服务器上传二进制文件 自动指定 content-type是 *form-data的形式，
	curl -F 'file=@test.jpg' taobao.com -v 
	curl -F 'file=@cookies.txt;type=text/plain' taobao.com -v
	还可以指定上传文件的MIME类型，否则会将文件类设置为application/octet-stream
-G get请求携带参数
	curl -G -d 'keywords=iphone' https://s.1688.com/selloffer/offer_search.html
	如果数据中有中文或空格，还可以使用 --date-urlencode 做编码处理
	curl -G --data-urlencode 'keywords=苹果手机' https://s.1688.com/selloffer/offer_search.html
-H 指定请求头信息
	$ curl -d '{"login": "emma", "pass": "123"}' -H 'Content-Type: application/json' http://localhost:4723
参考：
	https://linux.die.net/man/1/curl
	http://www.ruanyifeng.com/blog/2019/09/curl-reference.html
	https://catonmat.net/cookbooks/curl

-i 获取响应信息
-I 发送了一个 HEAD 请求获取响应头信息
-k 跳过ssl检测
-L curl默认不进行重定向，—L 会向浏览器一样进行自动定向
-s silent
-u 用来设置服务器认证的用户名和密码 curl -u 'bob:12345' https://google.com/login
-X 指定请求的方式
```

##### 2、postman

```shell
如何设置ssl证书：https://www.cnblogs.com/hailongchen/p/9902838.html
```

















