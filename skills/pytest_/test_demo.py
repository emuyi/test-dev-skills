"""
一、pytest 单元测试框架相比着 unittest 测试框架
    1. 用例的组织方式更加灵活，不需要继承 TestCase 之类的类，只需要
        a.放在以 test_* 或 *_test 的文件中
        b.以 test_* 开头的函数或者以 Test*开头的类且以 test_* 开头的方法，注意！测试类中不能有 __init__ 方法
    2. 断言的方式更加的灵活，支持python标准的断言语句，而不是像 xUnit风格的还有记相关的 API self.assert*
    3. 强大且灵活的 fixture，
    4. 兼容 unittest 语法

二、fixture
    用来处理测试用例执行前环境的初始化以及执行后环境的恢复。相比着 xUnit 架构将 setUp和 tearDown 集成到测试用例的方式，
    pytest.fixture 的使用更加灵活且功能更加强大。
    1. pytest.fixture 是一个装饰器，目前只能用来装饰函数和方法，如果给测试类加fixture可以使用mark.usefixtures
       fixture 将以形式参数的形式表明是某个测试用例或者fixture的依赖，并且将结果以实参的形式传递给测试用例。
    2. fixture 表示环境的初始化(setUp)。如果要处理环境的销毁和恢复(tearDown)，需要使用 yield，yield后面的语句是销毁的逻辑（实际上是利用了协程
    的原理，遇到 yield fixture挂起，执行测试用例，用例执行完毕，激活fixture协程进行环境的恢复） 示例：yield & addfinalizer
        问题：如何确环境最后得到恢复，不会对后续用例产生影响？
        1. 使用 request.addfinalizer(tearDownFunction) 代替 yield(官方不推荐)
        2. 优化 fixture 的编码结构，尽量使每个 fixture 是一个简单原子性操作，即一个setUp配一个setDown。不要将 fixture 逻辑变的过于复杂。
    3. fixture 有 scope，autouse，params，name，ids 等参数，每个参数的作用见下方。
    4. fixture 可以在 function, class, module, package, session 被共享，可以使用 fixture 装饰器的 scope参数来指定
         问题：fixture 的执行顺序？
          不同作用域：session > package > module > class > function
          同级作用域：要看测试用例及fixture的依赖关系。这里比较特殊的是，auto=True 的会自动执行，所以会先执行。
    5. fixture 也可以嵌套 fixture，但由于 pytest 会 cache fixture的返回值，也就是每个 fixture 只会执行一次，这样就避免了重复调用的问题。
      (类似 @functools.lru_cache) 如下方示例：fixture 嵌套 fixture。
    6. 问题：测试类外的 fixture 可以使用某个测试类内的 fixture么？ 答：依赖fixture的测试用例也在测试类中就可以。因为pytest是从测试用例的
        角度看待一个fixture是否可以用，只要我用例能找的到，那就ok。示例：outer fixture 调用 inner fixture
    7. conftest.py 实现 fixture的跨文件共享，即定义在 conftest.py 中的 fixture 可以直接拿来用，不用再进行导入。
       项目级别的 contest.py 被整个项目共享，当然每个 package也可以有自己的 conftest.py
    8. ！！！！参数化的 fixture
        当测不同参数选项的功能时，常用参数化的fixture来做初始化。即 fixture(params=[arg1, arg2]) 有点类似一个for 遍历这个参数列表
        分别执行fixture和用例。示例：参数化的fixture
    9. fixture的参数之一：ids, 在参数化fixture中，可以使用命令行 -k 参数配置 ids来指定执行某个用例。 示例：指定执行某个用例

三、mark
     通俗理解 pytest.mark 装饰器，就是给测试用例做标记，如 pytest.mark.xfail 标记用例期望失败。mark.skip 标记用例跳过等
     常用的内置mark：
        1. pytest.mark.usefixtures(fixture1, fixture2)
           给测试类标记使用哪个fixture；或者要使用多个fixture时
        2. pytest.skip(reason='xxx') 和 pytest.skipif(condition, reason='xxx')
           无条件跳过某个用例和根据条件跳过某个用例
        3. pytest.mark.xfail(condition, reason='xxx', run=False, strict=True, raises=具体的异常)
            标记一个用例为期望失败，即当用例执行失败后，不显示用例 fail，而是 xFail， 当用例执行没问题，标记为 xPass
            condition: 在某种条件下进行标记
            reason: 标记的理由
            run=False：直接标记，不执行测试用例  等同于 pytest.xfail(reason=xxx)
            strict=True：即便是用例执行成功了，也报用例执行失败即 Fail。
            raises：可以指定具体的异常类型。
        4. pytest.mark.parametrize('test_input, expected', [("1+2", 3), ("3+4", 7), ('5+6', 12)])
            其中 xfail 和 skip 常和 parametrize 混合使用，即作为其中的一个参数
            pytest.mark.parametrize('test_input, expected', [("1+2", 3), ("3+4", 7),
            pytest.param("5+6", 12, marks=pytest.mark.xfail)
        5. pytest.mark.filterwarnings('ignore:warning info')
           主要用例处理被测功能的warning信息。如报warning该怎么处理，因为pytest虽然不会报用例fail，但会显示 warning
     pytestmark 全局变量：
            当标记整个模块的测试用例是可以使用 如pytestmark = pytest.mark.skip
            当标记整个类的测试用例时可以使用 如pytestmark = pytest.mark.xfail 作为类方法 或者直接使用装饰器形式装饰这个类。

        ！! mark相关的示例见 test_mark.py

四、pass

、命令行参数
    -v 输出详细信息
    -s 输出print或logging信息
    -q 输出简单的执行信息
    --capture=no 实时显示执行信息
、其他
    1、处理被测功能抛异常的情况
    pytest.raises(ErrorType, match=regex)

    2、自定义标记mark只执行部分用例
        pytest.mark.webtest / 命令行 -v “webtest”  并且支持逻辑上的 and not or
"""
import pytest


# 使用函数组织测试用例
def test_case():
    assert 1


# 使用类组织测试用例
class TestCase:

    def test_upper(self):
        assert 'hello'.upper() == 'HELLO'


# fixture 嵌套 fixture
@pytest.fixture
def item_one():
    return 'item1'


@pytest.fixture
def order():
    return []


@pytest.fixture
def add_item_to_order(item_one, order):
    order.append(item_one)


def test_add_item(add_item_to_order, order, item_one):
    print(order)   # 如果 order 被重复调用的话，这里的 order 应该是 [], 而非[item1]
    assert order == [item_one]


# yield & addfinalizer
@pytest.fixture
def goods():
    return 'goods'


@pytest.fixture
def cart():
    return []


@pytest.fixture
def add_good_to_car(goods, cart):
    cart.add(goods)
    yield
    cart.clear()


# 注意这里的 request 是 pytest 传给 fixture的请求上下文对象， 通过 request 对象可以内省依赖fixture的测试用例，如 调用
# request.function/request.module 可以查看请求该fixture的测试用例的信息。同时在参数化fixture中，request.param 用来
# 表示具体参数。
@pytest.fixture
def add_good_to_car(request, goods, cart):
    cart.append(goods)

    def clear_cart():
        cart.clear()
    request.addfinalizer(clear_cart)


def test_add_good(add_good_to_car, cart):
    assert cart == ['goods']

# outer fixture 调用 inner fixture


@pytest.fixture
def two():
    return 2


@pytest.fixture
def outer(inner):
    return inner


class TestCase2:
    @pytest.fixture
    def inner(self, two):
        return [two]

    def test_method01(self, outer, two):
        print(outer)
        assert outer == [2]


# 参数化的fixture

@pytest.fixture(params=['param1', 'param2'])
def params_fixture(request):
    return request.param


def test_params_fixture(params_fixture):
    print(params_fixture)

"""
test_demo.py::test_params_fixture[param1] param1
test_demo.py::test_params_fixture[param2] param2
"""


# 示例：指定执行某个用例(-k & ids)
@pytest.fixture(params=[0, 1], ids=['param_one', 'param_two'])  # 注意 ids 一般是一个字符串的序列，一一对应着params中的元素
def params_fixture1(request):
    return request.param


def test_params_fixture1(params_fixture1):
    print(params_fixture1)


# pytest -s -v -k param_one test_demo.py
