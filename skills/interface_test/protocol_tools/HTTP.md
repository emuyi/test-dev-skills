#### 概述

```python
HTTP 协议是一种简单的请求-响应式协议，它属于 TCP/IP 协议族的一种，主要规定了客户端和服务端之间通信的格式。如以一个简单的GET请求为例：
----------request-----------------
    GET / HTTP/1.1            ---> 请求方式 请求URI 协议版本
    Host: www.taobao.com
    User-Agent: curl/7.68.0     ---> 请求头部字段信息
    Accept: */*


----------response------------------

    HTTP/1.1 301 Moved Permanently     --->协议版本 状态码 状态描述
    Server: Tengine
    Date: Wed, 20 Jan 2021 11:14:31 GMT  --->相应头部信息
    Content-Type: text/html
    Content-Length: 278
    Connection: keep-alive
    Location: https://www.taobao.com/
    Via: cache6.cn2581[,0]
    Timing-Allow-Origin: *
    EagleId: dde5cb8816111412716095529e
                                          ----> 头部信息和数据通过空行(\r\n)隔开
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <html>
    <head><title>301 Moved Permanently</title></head>           ---> 响应数据
    <body bgcolor="white">
    <h1>301 Moved Permanently</h1>
    <p>The requested resource has been assigned a new permanent URI.</p>
    <hr/>Powered by Tengine</body>
    </html>

# http 1.0 和 http 1.1 的区别：
	1、 1.0是短连接，即每次请求和响应都需要重新创建tcp连接，如果需要复用连接需要加上头部信息：Connection：keep-alive
	1.1 默认进行持久连接，同时引入了pipelining管道机制，允许客户端同时发送多个请求；并新增了PUT、DELETE、OPTIONS等请求方式
```

#### 请求方式

```python
GET：获取资源 select
POST：向服务端发送数据比如表单数据 create
PUT：类似于POST，不过是对服务器上的资源进行更新 update
DELETE：删除指定资源 delete

HEAD：类似GET，不过返回只有响应头，没有具体的数据
OPTIONS：可以查看服务端的对资源的支持情况，如都支持哪些头部信息，支不支持跨域，场景：cros跨域的时候，会先用
发送 OPTIONS 做下预检 http://www.ruanyifeng.com/blog/2016/04/cors.html
    
# GET请求和POST请求的区别
	1、GET常用来获取资源，而POST常用来给服务端发送数据.
    2、如果GET请求想要携带参数，通常情况下是以查询字符串的形式拼接在url里，而POST通常放在请求体内
       但这个并不是 HTTP 协议规定的内容，当然GET请求的参数也可以放在请求体中，POST请求的数据塞到URL里
       但一般情况下大家都不这么用。
```

#### 状态码

````
状态码：用来表示请求能否被正常处理，HTTP协议状态码分为5大类：
查阅参考:https://www.runoob.com/http/http-status-codes.html
1xx 信息性状态码
2xx 请求被正常处理
	200 ok 正常的处理了请求且返回了资源
	204 no content 请求被正常处理，但没有资源可以返回
	206 partial content 处理范围请求
3xx 重定向
	301 moved permanently 永久重定向。表示请求的资源被永久移到了新的 uri, 往往返回的信息里会携带新的uri(响应头里的Location) 浏览器会自动定向到新的uri。如：curl www.taobao.com
	302 Found 临时重定向，和301类似 但不是永久的，是临时，意味了已经移动的资源未来还有可能被改
4xx 客户端错误
	400 bad request 请求报文中有语法错误
	404 Not Found 服务端没有请求的资源或者不想让访问
	403 Forbidden 拒绝访问
	401 Unauthorized 认证失败 如登录失败的时候
5xx 服务端错误
	500 Internal Server Error  服务端bug了
	503 Service Unavailable 服务端超负载了或者停机了
	502 Bad Gateway 充当网关或者代理角色的服务器，从它上游服务器收到了一个无效的响应
````

#### 头部信息

```python
查询参考：http://tools.jb51.net/table/http_header
常见的请求头：
	Host：请求的域名
    Accept：客户端能够接受的内容类型，对应响应头里面的Content-Type
    Cookie: $Version=1; Skin=new; 发送请求的时候客户端会带着cookie一块请求
    Content-Type：post请求指定数据的类型
    常见的类型：application/x-www-form-urlencoded; application/json;multipart/form-data(文件上传)
    Content-Length：post请求数据的长度 (字节)
    Referer：来源
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win6.. 用户代理
常见的响应头：
    Server: Apache/1.3.27 (Unix) (Red-Hat/Linux)
    Content-Encoding: gzip
    Content-Type: text/html;text/css;appliaction/json;
    Content-Length: 278
    Connection:keep-alive 不过1.1版本默认就是持久连接
    Set-Cookie: UserID=JohnDoe; Max-Age=3600; Version=1 设置cookie
    Location: 301 重定向的时候回用来指明新的url
```

#### SSL加密

```python
HTTPS = HTTP + 加密 + 认证 + 完整性保护
    加密：指的是双方通信的过程是不是明文，而是经过加密的
    认证：指的是通信双方对对方都做了一个确认，确认对方都是真实存在且可靠的
    完整性保护：指的是传输的数据不会再中途被拦截篡改
本质是：HTTP 的通信接口层套上了一层 SSL 协议的外壳，使原本直接就可以和TCP进行通信变成了先要同SSL通信再由SSL与TCP通信
加密技术：
	非对称性加密，即公钥和私钥，公钥是公开的，而私钥是私有的，通过公钥加密的数据，只有通过对应的私钥才能解开。
	比如：使用本地 git 连接 github的时候获取的公钥和私钥。
认证：数字证书，用来确认公钥的身份是可信赖的，多数浏览器都会内嵌很多根证书。
HTTPS的不足点: 加密解密要消耗系统资源，所以在通信效率上不如 HTTP，另外买证书也很贵。
```

#### cookie、session、token

```python
cookie、session、token 都是处理http协议的是一种无状态协议，不会保存用户会话状态的一种技术手段

cookie：
	    当用户(指浏览器)首次访问服务端的时候，服务端会将用户状态信息设置cookie(如响应头的set cookie)，发送给用户
    	用户将cookie保存在本地，以后每次访问都会在请求里携带cookie。
		
		#cookie 重要的属性
         - name=value 设置cookie对应的命令和值，但是必须都得是字符串类型。
         - domain 指定cookie所属的域名，默认是当前域名
		 - path 指定cookie在哪个路径下生效，默认是 /
         - maxAge 失效的时间 单位是 s
         - expires 过期时间 在设置的时间点后失效
         - secure 如果 secure 为 true，cookie 只能在https中生效，默认是false
		 - httpOnly 如果设置了httpOnly，就无法通过js来获取cookie的信息（xss攻击）
session:
        session的话，是指用户的相关信息放在服务端保存，当用户登录成功后，会返回一个seesionId，并写入到用户cookie
        里，稍后用户请求，服务端会从用户的cookie信息里来获取sessionId得知用户身份并进行后续的操作。
       	session相比着cookie, 由于是保存在服务端所以安全性更高，支持存储的数据类型更广泛，存储能力也更强。
token:
    	session 是在服务器上存储用户信息，如果用户请求越来越多，对服务端造成的压力比较大。
        token的话，是指用户信息不再保存在服务器，而是通过加签处理发送给客户端，由客户端保存。
        主要的流程是这样的：
        	用户输入账号密码进行登录，服务端认证通过后，将用户信息通过一些hash算法(sha256)之类的做下加签处理，然后返回
            给客户端(localstoarge/cookie), 之后客户端的每次请求都会携带token，然后服务器对token进行解密和验证，然后
            执行后续的操作。
         token相比着sesion的好处：
        	1、减轻服务端的存储压力
            2、便于服务器端业务的扩展，比如说要做负载均衡，要做集群，由于用户访问会自带自己的信息，就不用考虑着扩展的服务器上也
            考虑保存用户相关的信息
            3、token可以不用写入到cookie，从而也可以解决跨域请求的问题。
            	请求头里面携带token
                	(Authorization: Bearer <token>  JWT）
参考：https://juejin.cn/post/6844904034181070861
     http://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html
```

![image-20210121135156208](C:\Users\MUYI\AppData\Roaming\Typora\typora-user-images\image-20210121135156208.png)

https://blog.csdn.net/kongmin_123/article/details/82555936

