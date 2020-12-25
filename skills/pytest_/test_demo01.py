"""
1. 断言上更加灵活，可以通过python运算符号， 而不是self.assert*
2. 自动查询用例，而不是需要将用例加到测试套件中或者继承某个类。
    默认是从根目录(可以配置或者参数指定)下查找 test_* 或 *_test的py文件，从中收集
    test开头的函数或者Test开头的类里面是test_*的方法，注意这样的类不能有__init__ 方法
    并且兼容 unitttest 语句
3. pytest.raises(exception, match=regex)
    pytest会使用一个上下文管理器来处理被测功能抛异常的情况
    异常可以是具体的异常类型，如不不知道具体是哪个异常，可以指定 match参数匹配异常信息。（可以用正则表达式）
    并且可以获取具体的异常信息
    with pytest.raises(Exception, match='^x') as exc_info:
    func(2)
    assert 'x' in exc_info.value.args[0]
4. 灵活的fixture
    a. 首先兼容 xUnit setUp和 tearDown 风格的 fixture 方式
    b. fixture 的设计理念：
        首先，一个测试用例如何知道它需要用例什么样的fixture？ 传统的 xUnit 风格： 把 fixture 分别放在我的测试步骤前后就行了。
        也就是说， fixture是集成在我的测试用例中的。
        而 pytest 则把 fixture 作为测试用例的参数，由测试用例 “请求” 我需要的 fixture，首先这实现了编码的解耦，其次也让 fixture
        的使用变的更加灵活，如整个测试项目级别的fixture，模块级别的 fixture
    c. fixture 的使用原理：
        pytest 通过测试用例的形式参数，检测是否有同名的 fixture 函数(即由pytest.fixture 装饰的函数），如果有，则调用它并将它的返回值做
        为测试用例的实参传递给测试用例。

    d.




命令行参数：
    -q 简单输出打印信息
    -v 打印详细信息
    -s 显示 print 和 logging 的信息
   --capture=no 实时打印用例执行信息（包括内部的print和loggin信息）

"""
import pytest

# def test_upper():
#     assert 'hello'.upper() == 'UPPER'


def f(x):
    return x


class TestClass:

    # def test_xx(self):
    #     assert 1 == 2

    def test_f(self):
        assert f(1) == 1


















