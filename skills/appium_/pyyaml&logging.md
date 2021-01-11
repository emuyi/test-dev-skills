#### YAML 语法

```yaml
yaml 是一种文本标记语言，常用来存储结构化数据或做配置文件。
基本的语法规定：大小写敏感；使用缩进来表示层级关系；使用空格来缩进，几个空格不重要，对齐就行。
常用的数据结构的写法：
	1、 --- 表示 yaml 文档流的开始，... 是一个可选的文档流结束的标记。单个文档可以不用 --- 来标记文档流
	    包含 --- 标记为显示文档，不包含的为隐式文档
	
	2、数组表示
        - a
        - b
        - c
        - d
       或者
        -
          - 1
          - 2
          - 3
        -                      
          - 7
          - 8
          - 9
      或者
        - - 1
          - 2
          - 3
        - - 7
          - 8
          - 9
    3、字典表示
        ---
        a: 1
        b: 2
        c: 3
        ---
        A:
          - 1
          - 2
        B:
          - 3
          - 4
        ---
        C:
          key: value
        D:
          key: value
	4、其他数据
		字符串，布尔值，整数，浮点数，null(~)，日期

python 操作 yaml 文件：pyymal，用法和 json 很像， yaml.safe_load(stream) / yaml.dump(pyObject)
https://www.runoob.com/w3cnote/yaml-intro.html
https://blog.csdn.net/swinfans/article/details/88770119
```

#### Logging

```python
import logging


class LoggingUtils:

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        fh = logging.FileHandler('running_log.txt', encoding='utf-8')  # file handler 用于将日志输出到文件
        sh = logging.StreamHandler()  # stream handler 将日志输出到 console
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s - %(message)s', '%Y-%m-%d %H:%M:%S')  # 设置日志样式
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self._logger.setLevel(logging.DEBUG)  # 注意：logger 对象也是设置下 level，默认是 warning
        fh.setLevel(logging.INFO)  # 给 fh，sh 设置级别
        sh.setLevel(logging.INFO)
        self._logger.addHandler(fh)  # logger对象可以添加多个fh和sh对象
        self._logger.addHandler(sh)

    @property
    def logger(self):
        return self._logger


logger = LoggingUtils().logger

https://www.jb51.net/article/88449.htm
```



