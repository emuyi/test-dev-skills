import pytest
from pytest import ExitCode


# 使用类组织, pytest.raises 处理被测函数异常
def func(x):
    if x == 1:
        raise(IndexError('index out of range'))
    elif x == 2:
        raise (Exception('xxx'))


class TestCase002:
    def test_func(self):
        with pytest.raises(Exception, match='^x') as exc_info:
            func(2)
        assert 'x' in exc_info.value.args[0]











