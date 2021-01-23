"""
requests 框架的文档写的非常好，通读文档就对啦！
docs：https://requests.readthedocs.io/zh_CN/latest/
帮助练习requests 的网站：https://httpbin.testing-studio.com/
1、快速上手
    请求相关
        - 请求方法：requests.get .post .put .delete .head
        - get请求携带参数：params={key:value, key1:[value1, value2]}
        - post请求发送数据：(data参数指定)
                1、默认是发送的编码 *form-urlencoded数据, 即发送的是表单数据
                2、处理checkbox, select 之类的标签数据呢？ data=((key, value1), (key, value2))
                3、发送json数据，data=json.dumps(data_dict) or json=data_dict
                4、上传文件，files={files:open(xx, rb)} 文件类型是 application/octest-stream **
                   显示指定上传文件的类型，files={files:(file, open(), image/jpg)}
        - headers参数 指定请求头
        - timeout参数，指定连接超时的时间
        - 除了 head 请求，默认自动重定向，即 allow_redirects 默认是 True的，如果要禁止重定向，allow_redirects=False即可
          可以通过 r.history 获取访问历史
    响应相关
        - 状态码
            r.status_code
            r.raise_for_status 指 4xx， 5xx时候回抛出异常
            此外，内部还维护了一个包含状态码和描述的 codes字典，requests.codes, 如通过requests.codes.ok 是否是 true来判断请求的是否成功
        - 响应头
            r.headers
        - 响应体
            r.text 解码处理后的文本 【如果解码失败，可以通过r.content 来看返回内容设置的编码，然后使用 r.encoding进行编码设置】
            r.content 字节数据
            r.json()
            r.raw() 原始套接字数据
    cookie相关
            1、请求携带cookie， 指定cookies={name：value}
            2、r.cookies 获取服务端设置的cookies，
            3、r.cookies 是一个 RequestsCookieJar 对象，类似字典，但封装了更多的功能，比如跨域或者跨路径携带
            cookie，本质是给cookie的domain,path 属性赋值
              jar = requests.cookies.RequestsCookieJar()
              jar.set('name', 'bobby', domain=host.split('//')[-1], path='/cookies')
2、进阶用法

3、身份认证

"""
# ===================================快速上手=====================================================
# https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html
# -------------------------------------请求相关----------------------------------------------------
import requests
from requests.cookies import RequestsCookieJar
from requests.utils import add_dict_to_cookiejar
from requests.auth import AuthBase

chrome = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

data = dict(
    name='ellen',
    passwd='123'
)

payload = dict(
    wd='requests的用法',
    a='b',
    c=[1, 2]
)

headers = {
    'user-agent': 'emuyi'
}
host = 'https://httpbin.testing-studio.com'

# post请求
# 默认以form表单提交参数的形式传数据
# 1.data={a:1, b:2}
# 2.data=((key1, value1), (key2, value2))   # 处理 checkbox select类型表单
# 3.发送json数据  a.data=json.dumps(data_dict); b. json=data_dict
# 4.发送文件(multipart-formdata)，指定files = {'files': open(a.txt, rb)}
# 如果不指定文件类型，默认application/octet-stream;base64进行编码，显示指定类型的话 {files:(test.jpg, open(test.jpg, rb), image/jpeg}
# todo 文件上传需要实际操作
# r = requests.post(host + '/post', files={'files': ('test.jpg', open('test.jpg', 'rb'), 'image/jpeg')})
# print('***', r.text)

r = requests.post(host + '/post', data=data)
print(r.json().get('form'))

# 查询字符串(get请求带参数的常用)
res = requests.get(host + '/get', params=payload)
print(res.url)

# 关于请求头 headers 参数
# 需要注意的是，requests 会负责把定制的headers 全部传递，但不一定所有的定制headers都会生效，要具体分析
# https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html#id6

r = requests.get(host + '/get', headers=headers)
print(r.text)
# -------------------------------------响应相关----------------------------------------------------
# 关于响应数据
# r.text 以文本的形式返回响应的数据， r.content 是以字节的形式返回
# r.text 会自动解码，但是如果解码出现了问题，可以通过 r.content 来查看返回的html或xml(应该会有编码的指定)
# 然后使用 r.encoding=xxx, 来指定编码
# r.json() 服务端返回的数据是json的话，使用r.json(), 且也将json数据直接load成dict了
# r.raw 获取原始的套接字响应，需要设置 stream=True 参数 通过 iter_content 来获取 [r.raw]
"""
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
"""

r = requests.get('https://www.cnblogs.com')
# print(r.content)

r = requests.get('https://www.cnblogs.com')
print(r.status_code)

# 关于状态码
# r.status_code 来表示，如果返回的是 4xx，5xx的状态码的话，可以使用r.raise_for_status 抛出异常
r = requests.get('https://www.baidu.com/login')
print(r.status_code)
print(r.status_code == requests.codes.all_ok)  # requests 内部维护一个关于状态码以及状态码描述的_codes 字典
try:
    r.raise_for_status()
except Exception as e:
    print(e)

# 关于响应头，可以通过 r.headers 获取响应头信息字典，并且遵循 RFC 2616规定，对大小写不敏感
print(r.headers)  # {'Content-Length': '203', 'Content-Type': 'text/html; charset=iso-8859-1'}
print(r.headers.get('content-type'))
# -----------------------------------cookie相关-------------------------------------------------
# 1、通过 r.cookies 可以获取服务端设置的cookie
r = requests.get('https://www.baidu.com', headers={'user-agent': chrome})
print(type(r.cookies))
print(dict(r.cookies))   # RequestsCookieJar对象 类似字典
print(r.cookies.get('BAIDUID'))
# 2、get请求的时候携带 cookie 可以指定cookies参数
r = requests.get(host + '/cookies', cookies=data)
print(r.text)
# 3、通过 RequestsCookieJar 可以实现跨域或跨路径携带cookie， 因为cookie只能在指定的域或者路径下生效
# 感觉这块应该是通过指定cookie的属性来实现的 如(domain, path, maxAge, expires, secure, httpOnly)
jar = RequestsCookieJar()
jar.set('name', 'bobby', domain=host.split('//')[-1], path='/cookies')
jar.set('name', 'hanks', domain=host.split('//')[-1], path='/get')
r = requests.get(host + '/cookies', cookies=jar)
print(r.text)

# ------------------------------------重定向相关--------------------------------------------------
# 1、除了 HEAD 请求，requests 默认是自动重定向的，原因是里因为控制是否重定向的参数 allow_redirects 默认是 True
# 所以如果想禁止重定向，allow_redirects = False, 同理如果HEAD 请求想要自动重定向，get请求的时候设置 allow_redirects = True
# 2、r.history 重定向的历史，它返回的是 response 对象的列表，按照访问历史由老到新进行排序
r = requests.get('http://www.taobao.com')
print(r.status_code)
# print(r.history[0].status_code)

# ------------------------------------timeout参数--------------------------------------------------
# ，指定连接超时时间(注意timeout限制的不是响应体下载的时间，而是建立连接的时间)
# 如果没有设置 timeout 参数，比如要访问网站网络不通，它会夯住，直到底层的urllib3 抛错，如目标计算机拒绝访问之类的
r = requests.get('https://www.baidu.com')
print('*' * 200)
# ===================================进阶用法=====================================================
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html

# ------------------------------------会话对象 Session()--------------------------------------------------
# 会话对象 requests.Session() 跨请求的时候保持某些参数

# 1.保持cookies (登录后能正常的访问其他页面而不必重新登录)
s = requests.Session()
r1 = s.get(host + '/cookies/set/freeform/aaa')
r = s.get(host + '/cookies')
print(r.text)
# 2. 注意只有会话级别的cookie才能在会话区间进行保持，方法级别设置的cookie不会被保持
r = s.get(host + '/cookies', cookies={'a': '1', 'freeform': 'bbb'})
print(r.json())  # {'cookies': {'a': '1', 'freeform': 'bbb'}}
r = s.get(host + '/cookies')
print(r.json())  # {'cookies': {'freeform': 'aaa'}}
# 3.会话界别设置cookie requests.utils.add_dict_to_cookiejar(cj, cookie_dict)
add_dict_to_cookiejar(s.cookies, {'name': 'bobby'})
# 4.给请求方法设置默认参数 如头部信息
s.headers.update({'server': 'emuyi'})  # 设置了一个默认的头部信息，之后所有的会话发送的请求都会携带
r = s.get(host + '/headers', headers={'server': 'bobby'})   # 但方法级别如果设置了同名的信息，方法级别会覆盖会话级别
print(r.text)
# 5、可以放在 with 语句块中做上下文管理 确保会话期间出现异常退出时，会话也能被关闭
with requests.session() as s:
    s.get('https://www.baidu.com')
# 6、如果会话层的某些键的数据不想要，可以在方法层将该键的值设置为None

# ------------------------------------响应对象包含请求对象--------------------------------------------------
# requests.get() 做了两件事，1.创建一个request对象，去某个服务器上请求资源，2.服务器响应返回一个response对象，response对象
# 中既包含响应的资源，也包含请求的对象request，如何去访问它，只需r.request 即可

r = requests.get('https://www.baidu.com')
print(r.request.headers.get('user-agent'))  # <PreparedRequest [GET]>

# ------------------------------------PreparedRequest-------------------------------------------------------
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#prepared-request
# requests发送的请求都是一个PreparedRequest对象，简单理解PreparedRequest 对象它是一个封装好了请求头，请求数据，cookies等数据
# 的请求对象，是对request.get 等请求的偏底层的解释
"""
requests.get 的源码流程
    无论是get请求还是 post请求，本质上都会走 session.request(method, url, data, headers...)
    session.request 拿着这些参数实例化 req = Request(method, url, data, headers...) 对象
    再去调用 prepare_request(req) 方法构造 PreparedRequest() 对象，最后走 session.send(prepped) 
"""
# 如以下示例：
r = requests.get('https://www.baidu.com')
# 用偏底层的写法来写的话
s = requests.Session()
req = requests.Request('GET', 'https://www.baidu.com')
prepped = s.prepare_request(req)
# prepped.prepare_body()
# prepped.prepare_header()
res = s.send(prepped)

# ------------------------------------SSL 证书验证-------------------------------------------------------------
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#ssl
# 像浏览器一样， requests默认是开启SSL认证的, 如果认证失败，可以把证书通过 verify 参数指定证书路径，或者放到 REQUESTS_CA_BUNDLE环境变量里
# 或者将 verify 设置为 False
# os.environ.get('REQUESTS_CA_BUNDLE')
# os.environ.get('CURL_CA_BUNDLE')
# 如果一个网站的根证书是受信任的，那么他的子证书都是可信任的，对于浏览器来说，它会通过证书链去找这个网站的根证书，然后确认是不是自己信任的根证书机构
# 颁发的  “由于CA 根证书不在“受信任的根证书颁发机构”存储区中，所以它不受信任。” --- 出自 google
# r = requests.get('https://inv-veri.chinatax.gov.cn/')

# requests 内嵌了一套受信任的根证书，来源于 Mozilla trust store，这些证书只有在requests更新的时候才会被更新，所以要尽量保持requests时常
# 更新，同时requests也会使用 certifi 库里的证书，也要尽量保持 certifi 的及时更新。

# ------------------------------------流式下载(下载大文件)-------------------------------------------------------------
# 默认情况下 requests 是立即下载响应体，文件比较的大的时候可以指定 stream=True 进行流式下载，
# 当 stream = True的时候，requests会将延迟下载，这时可以使用iter_content(trunk_size), iter_lines(trunk_size)
# 按照指定大小下载文件。

# ! 需要注意的是，如果使用 stream=True 意味了着 Requests就没办法将连接释放回连接池，除非数据被全部接受完毕，或者显示调用 response.close()
# 因此为了确保连接能够最终被释放，建议通过 with 语句来进行上下文的管理
# with requests.get('https://github.com/kennethreitz/requests/tarball/master', stream=True) as r:
#     with open('a.zip', 'wb') as f:
#         for trunk in r.iter_lines(1024):
#             print(trunk)
#             # f.write(trunk)
# ------------------------------------流式上传(上传大文件)-------------------------------------------------------------
# with open('big-data', 'rb') as f:
#     requests.post('http://some.url/streamed', data=f)

# ------------------------------------多文件上传---------------------------------------------------------------------
# multiple_files = [
#     ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
#     ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))
# ]
#
# r = requests.post(host + '/post', files=multiple_files)
# print(r.text)
# ------------------------------------hook---------------------------------------------------------------------
# 目前还是只接收 response 这一个 hook，所以可以通过 hook做一些响应检查或者修改响应的某些信息


def callback(response, *args, **kwargs):
    print(response.url)
    response.url = 'https://www.taobao.com'
    response.status_code = 500
    return response


r = requests.get('https://www.baidu.com', hooks=dict(response=callback))
print(r.url, r.status_code)

# ----------------------------------自定义身份认证 Custom HTTP Auth-----------------------------------------------------
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#custom-auth
"""
:param auth: (optional) Auth tuple or callable to enable

            Basic/Digest/Custom HTTP Auth.
"""


class PizzaAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['X-Pizza'] = self.username
        return r


# requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))

# ----------------------------------流式API-----------------------------------------------------
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#streaming-requests
# TODO 需要一个场景
# 处理方式：通过r.iter_lines() 和 r.iter_content() 进行处理
# ----------------------------------代理-----------------------------------------------------
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#proxies
# socks代理 https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#socks
# TODO 需要一个场景

# proxies = {
#     'http': 'http://192.168.0.105:8888',
#     'https': 'https://192.168.0.105:8888'
# }
#
# r = requests.get('https://baidu.com', proxies=proxies)

# ----------------------------------响应体解码----------------------------------------------------
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#id16
# 1、响应头里推测编码方式 2、charade库尝试进行解码 如果还是解码失败，可以通过手动指定 r.encoding 来指定解码方式或者
# 使用 r.content 原始字节

r = requests.options(host+'/cookies')
print(r.status_code)
print(r.headers.get('allow'))

# ----------------------------------支持所有的http请求动词，甚至支持定制动词--------------------------------
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#id17

# --------------------------------响应头链接字段-------------------------------------------------------
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#link-headers

# ----------------------------------传输适配器-------------------------------------------------------
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#transport-adapters

# ----------------------------------requests是阻塞式的-------------------------------------------------
# 基于requests的异步框架：
#   grequests https://github.com/kennethreitz/grequests
#   requests-future https://github.com/ross/requests-futures

# ---------------------------------- header 排序----------------------------------------------------
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html#header

# ----------------------------------timeout的再次说明-------------------------------------------------
# requests的里的timeout， 有两个：连接超时；读取超时
# 连接超时指的是客户端和服务端创建连接，request要等多长时间，即 socket，connect()
# 读取超时是服务端给客户端发送第一个字节的时候，request要等多场时间，即 socket，read()
# timeout = 5 ： 会用作 connect 和 read 超时时间
# timeout = (3.05, 10)  3.05: connect, 10: read


# ===================================身份认证==========================================================
# https://requests.readthedocs.io/zh_CN/latest/user/authentication.html
# 1、HTTP Basic Auth
from requests.auth import HTTPBasicAuth

r = requests.get('https://api.github.com/user')
print(r.status_code)  # 401
r_authed = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('username', 'password'))
# 上面的auth参数可以直接简写成auth = ('username', 'password')

# 2、HTTPDigestAuth
from requests.auth import HTTPDigestAuth
url = 'http://httpbin.org/digest-auth/auth/user/pass'
requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
# 3、OAuth1 和 OAuth2 的认证
# requests-oauthlib库进行处理
from requests_oauthlib import OAuth1
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
  'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

# 4、以上都不行，定制认证方式，继承 BaseAuth， 在定制的认证类的__call__里实现认证的逻辑，可以参见之前的示例



