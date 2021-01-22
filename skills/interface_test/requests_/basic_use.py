"""
request框架的文档写的非常好，通读文档就对啦！
docs：https://requests.readthedocs.io/zh_CN/latest/
帮助练习request的网站：https://httpbin.testing-studio.com/
1、快速上手
2、进阶用法
"""
# ===================================快速上手=====================================================
# https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html
# -------------------------------------请求相关----------------------------------------------------
import requests
from requests.cookies import RequestsCookieJar

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
# r.raw 获取原始的套接字响应，需要设置 stream=True 参数 通过 iter_content 来获取
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

# 关于重定向
# 1、除了 HEAD 请求，requests 默认是自动重定向的，原因是里因为控制是否重定向的参数 allow_redirects 默认是 True
# 所以如果想禁止重定向，allow_redirects = False, 同理如果HEAD 请求想要自动重定向，allow_redirects = True
# 2、r.history 重定向的历史，它返回的是 response 对象的列表，按照访问历史由老到新进行排序
r = requests.get('http://www.taobao.com')
print(r.status_code, r.text)
# print(r.history[0].status_code)

# timeout 参数，指定连接超时时间(注意timeout限制的不是响应体下载的时间，而是建立连接的时间)
# 如果没有设置 timeout 参数，比如要访问网站网络不通，它会夯住，直到底层的urllib3 抛错，如目标计算机拒绝访问之类的
r = requests.get('https://www.baidu.com')

# ===================================进阶用法=====================================================
# https://requests.readthedocs.io/zh_CN/latest/user/advanced.html
