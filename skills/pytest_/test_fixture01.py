import pytest


# 简单的fixture
class Fruit:
    def __init__(self, name):
        self.name = name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_fruit_in_basket(my_fruit, fruit_basket):

    assert my_fruit in fruit_basket


# fixture 也可以嵌套 fixture
@pytest.fixture
def first_item():
    return 1


@pytest.fixture
def second_item():
    return 2


@pytest.fixture
def order(first_item, second_item):
    return [first_item, second_item]


@pytest.fixture
def expect_list():
    return [1, 2, 3]


def test_order(order, expect_list):
    order.append(3)
    assert order == expect_list


# cache fixture 的返回值，将多次调用 fixture 成为了可能且避免了大量重复调用带来的效率问题
@pytest.fixture
def third_item():
    return 3


@pytest.fixture
def empty_sql():
    return []


@pytest.fixture(autouse=True)
def append_item_to_sql(third_item, empty_sql):
    empty_sql.append(third_item)


def test_fixture_cache(third_item, empty_sql, append_item_to_sql):
    assert empty_sql == [third_item]

# 也就是说一个 test 里的 fixture 只执行一次， 无论你调用多少次， 有点类似functools.lru_cache装饰器


# 参数化的 fixture
# 使用 autouse 参数，可以自动执行 fixture。
def test_fixture_autouse(empty_sql, third_item):
    empty_sql.append(4)
    assert empty_sql == [third_item, 4]


# fixture error， 当fixture中出现异常，pytest会停止和它有关的fixture甚至是测试用例的执行。
# 使用 yield 实现 tearDown 环境销毁及恢复，只需要将相应语句放在 yield 后就可以。（注意tearDown的
# 顺序，刚好是整个fixture创建顺序的 reverse。）利用协程的原理
# 使用 yield 并不能保证整个环境能够得到安全恢复，有两种方式 1. 使用 request.addfinalizer 2.
# 从 fixture 的编码上做调整，即尽量使每一个fixture都是一个简单的操作并且yield后面有明确的tearDown操作
# 和它对应。

@pytest.fixture
def item():
    return 'item'


@pytest.fixture
def cart():
    return []


# @pytest.fixture
# def append_item(item, cart):
#     cart.append(item)
#     yield 1
#     cart.clear()

# 也可以使用 addfinalizer 用来进行环境恢复, 即 request.addfinalizer(clearUpFunction)
# request 对象，它可以内省请求该fixture的测试用例，即通过request.function/module 可以直接获取到该测试用例的一些信息
# 如测试用例的名称之类的。

@pytest.fixture
def append_item(item, cart, request):
    cart.append(item)

    def clear_cart():
        cart.clear()

    request.addfinalizer(clear_cart)


def test_cart(append_item, item, cart):

    assert [item] == cart
# 关于 fixture 的可用性， pytest是从用例的角度去看待，只要我的用例能找到这个fixture就ok


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def outer(empty_list, inner):
    empty_list.append('outer')


class TestCase002:

    @pytest.fixture
    def inner(self, empty_list):
        empty_list.append('inner')

    def test_method(self, outer, empty_list):
        print(empty_list)
        assert ['inner', 'outer'] == empty_list


# 比照对象
# class TestCase003:
#
#     def test_method(self, outer, empty_list):
#         print(empty_list)
#         assert ['inner', 'outer'] == empty_list

# conftest.py 实现fixture的跨文件共享，也就是说将定义在conftest.py 中的 fixture 可以拿来直接使用，不需要进行导入
# 项目级别的conftest.py 可以被整个项目共享，当然每个package也可以有自己的conftest.py


# 关于 fixture 执行顺序
"""
1. 不同作用域：高作用域优先级高，即 session > package > module > class > function
2. 同级别作用域： 看测试用例以及fixture的依赖而定
3. 同作用域下 autouse 的先执行
"""


@pytest.fixture
def new_order():
    return []


@pytest.fixture
def a(new_order):
    new_order.append("e")


@pytest.fixture
def b(a, new_order):
    new_order.append("f")


@pytest.fixture(autouse=True)   # 我不管你测试用例依赖什么， efg 永远在 new_order 首位
def c(b, new_order):
    new_order.append("g")


@pytest.fixture
def d(b, new_order):
    new_order.append("a")


@pytest.fixture
def e(d, new_order):
    new_order.append("b")


@pytest.fixture
def f(e, new_order):
    new_order.append("c")


@pytest.fixture
def g(f, c, new_order):
    new_order.append("d")


def test_order_and_g(g, new_order):
    print(new_order)
    assert new_order == ["e", "f", "g", "a", "b", "c", "d"]

#





