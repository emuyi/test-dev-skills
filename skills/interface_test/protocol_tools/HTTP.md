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
   todo
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
    Cookie: $Version=1; Skin=new; 发送请求的时候客户端会带着cookies一块请求
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


http://www.ruanyifeng.com/blog/2016/08/migrate-from-http-to-https.html
```

#### cookie、session、token

```python

```



