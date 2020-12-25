import pytest


# autouse 示例二
@pytest.fixture
def order():
    return []


@pytest.fixture
def c1(order):
    order.append("c1")


@pytest.fixture
def c2(order):
    order.append("c2")


class TestClassWithAutouse:
    @pytest.fixture(autouse=True)
    def c3(self, order, c2):
        order.append("c3")

    def test_req(self, order, c1):
        assert order == ["c2", "c3", "c1"]

    def test_no_req(self, order):
        assert order == ["c2", "c3"]


class TestClassWithoutAutouse:
    def test_req(self, order, c1):
        assert order == ["c1"]

    def test_no_req(self, order):
        assert order == []

# 如何理解参数化的fixture，首先参数化的fixture主要是为了测试某个具有多种选项的模块。
# 有点类似for遍历执行fixture和testcase
# 用法：pytest.fixture(params=['xx', 'xx'])， 在fixture中可以使用 request.param 调用


@pytest.fixture(params=[0, 1], ids=['param1', 'param2'])
def param_fixture(request):
    return request.param


def test_param_fixture(param_fixture):
    print(param_fixture)

# 在参数化fixture中 ids 配合 -k 参数去指定某个用例执行, 注意 ids 是一个字符串指定的列表
# pytest -s -v -k  param1 test_fixture02.py


# mark.parametrize 参数化用例

# @pytest.mark.parametrize('input, expected', [("1+2", 3), ("3+4", 7), ('5+6', 12)])
# def test_mark_parametrize(input, expected):
#      assert eval(input) == expected


# mark 参数化中的参数还可以是一个mark
@pytest.mark.parametrize('test_input, expected',  [("1+2", 3), ("3+4", 7),
                                                  pytest.param("5+6", 12, marks=pytest.mark.xfail)])
def test_mark_parametrize(test_input, expected):
    assert eval(test_input) == expected



















