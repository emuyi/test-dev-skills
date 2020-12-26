"""
mark 是应用到测试用例上的和fixture没有关系
常用的内置mark：
    1.@pytest.mark.usefixtures(xxx, yyy)
      适用于给测试类添加 fixture 或者适用多个 fixture的场景
    2.@pytest.mark.filterwarnings("ignore:info") 如何处理被测功能报的warning，如果不处理，pytest不会判断用例fail，但会有warning信息
    3.@pytest.mark.skip(reason=xx) / @pytest.mark.skipif(condition, reason=xx) conditon 为 true 跳过
    4.@pytest.mark.xfail 标记一个用例是 期望测试用例是失败的，不用影响测试用例的执行，如果测试用例执行失败，report的时候是xfail，执行成功
    report的时候是 xpass
      @pytest.mark.xfail(condition, reason='xx', run=False, raises=具体的异常，strict=True(即便是执行成功了也标记用例失败)
    5.@pytest.mark.paramerize('input, expected', [(),(),pytest.param(marks)])
        xskip 和 xfail 可以用作 paramerize的参数 pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug"))

pytestmark 全局变量用来从模块级别或者类级别添加mark
    pytestmark = pytest.mark.usefixtures(xx) 从模块级别定义mark，模块中的所有用例都具备这个mark
    使用 类装饰器 或 pytestmark = pytest.mark.usefixtures(xx) 做为类属性，类中的所有测试用例都具备了这个mark

"""
import pytest
import warnings


def api_v1():
    warnings.warn(UserWarning("old api, should use new api"))
    return 1


@pytest.mark.filterwarnings("ignore:old api")
def test_one():
    assert api_v1() == 1


@pytest.mark.skipif(1 == 1, reason='should skip')
def test_two():
    assert 0


@pytest.mark.xfail(1 == 1, reason='1 == 1')
def test_three():
    assert 1


@pytest.mark.xfail(run=False)
def test_four():
    assert 0


@pytest.mark.xfail(raises=IndexError)
def test_five():
    assert [][10]


@pytest.mark.xfail(strict=True)
def test_six():
    assert 1


# 自定义标记mark执行部分用例
@pytest.mark.webtest
def test_web():
    assert 1


@pytest.mark.ios
def test_ios():
    assert 1


# 参数化
test_user_data=['linda','sai','tom']


@pytest.fixture(scope='module')
def login(request):
    user = request.param
    print('打开首页登陆%s'%user)
    return user


# indirect=True是把login当作函数去执行
@pytest.mark.parametrize('login', test_user_data, indirect=True)
def test_cart(login):
    usera = login
    print('不同用户添加购物车%s'%usera)
    assert usera != ''


