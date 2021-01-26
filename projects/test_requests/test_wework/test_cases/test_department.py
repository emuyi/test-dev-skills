import jsonpath
import pytest
from projects.test_requests.test_wework.api.department import Department
from projects.test_requests.test_wework.utils.common_tools import formatter, load_yaml

"""
使用 requests API的逻辑!!

class TestDepartment:

    test_create_depart_data = load_yaml('test_department.data').get('test_create_depart')

    @classmethod
    def setup_class(cls):
        cls.depart = Department()
        cls.depart.clear_env(cls.test_create_depart_data)

    @pytest.mark.parametrize('name', test_create_depart_data)
    def test_create_depart(self, name):
        ret = self.depart.create_depart(name=name)
        formatter(ret)
        assert ret.get('errcode') == 0

    def test_query_depart(self):
        ret = self.depart.query_depart()
        formatter(ret)
        assert ret.get('errcode') == 0

    def test_update_depart(self):
        ret = self.depart.update_depart(3, name='aaa')
        assert ret.get('errcode') == 0

    def test_delete_depart(self):
        # create first, assert, then delete, assert
        res = self.depart.query_depart()
        size_before = len(res.get('department'))

        self.depart.create_depart(name='测试部')

        res = self.depart.query_depart()
        assert len(res.get('department')) == size_before + 1

        ids = jsonpath.jsonpath(res, '$..department[?(@.name=="测试部")]')[0]['id']
        self.depart.delete_depart(ids)

        res = self.depart.query_depart()
        size_after = len(res.get('department'))

        assert res.get('errcode') == 0 and size_after == size_before

    @classmethod
    def teardown_class(cls):
        # do something
        pass

"""


# 测试步骤驱动化
class TestDepartment:

    test_create_depart_data = load_yaml('test_department.data').get('test_create_depart')
    test_delete_depart_step = load_yaml('test_department_step').get('test_delete_depart')

    @classmethod
    def setup_class(cls):
        cls.depart = Department()
        # cls.depart.clear_env([''])

    # 基于steps进行封装
    def test_delete_depart(self):
        self.depart.run_steps(self.test_delete_depart_step, 'test_delete_depart')

    @classmethod
    def teardown_class(cls):
        # do something
        pass
