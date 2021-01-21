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
todo

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

```

##### 2、postman

```shell
如何设置ssl证书：https://www.cnblogs.com/hailongchen/p/9902838.html
```

















