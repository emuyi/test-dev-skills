import requests
from jsonpath import jsonpath

from projects.test_requests.test_wework.api.wework import WeWork
from projects.test_requests.test_wework.utils.common_tools import load_yaml

"""
使用原生requests做API!! 
class Department(WeWork):

    _secret = 'xxx'
    _create_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
    _query_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
    _update_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
    _delete_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'

    def __init__(self):                      
        self._token = self.get_token(self._secret)

    def create_depart(self, name, parent_id=1, **kwargs):
        data = {'name': name, 'parentid': parent_id}
        data.update(kwargs)
        r = requests.post(self._create_url, json=data, params={'access_token': self._token})
        return r.json()

    def query_depart(self, **kwargs):
        params = {'access_token': self._token}
        params.update(kwargs)
        r = requests.get(self._query_url, params=params)
        return r.json()

    def update_depart(self, ids, **kwargs):
        data = {'id': ids}
        data.update(kwargs)
        r = requests.post(self._update_url, json=data, params={'access_token': self._token})
        return r.json()

    def delete_depart(self, ids):
        params = {'access_token': self._token, 'id': ids}
        r = requests.get(self._delete_url, params=params)
        return r.json()

    def clear_env(self, data):
        for item in data:
            res = self.query_depart()
            val = jsonpath(res, f'$..department[?(@.name=="{item}")]')
            if val:
                ids = val[0]['id']
                self.delete_depart(ids)

"""


# 测试步骤数据驱动

class Department(WeWork):
    """department management: crud"""

    def __init__(self):
        self._data = load_yaml('test_department.api')
        self._token = self.get_token(self._data.get('secret'))

    def create_depart(self, name, parent_id=1):
        kwargs = dict(
            params={'access_token': self._token},
            json={'name': name, 'parentid': parent_id}
        )
        r = self.send_request(self._data, 'create_depart', **kwargs)
        return r

    def query_depart(self):
        kwargs = dict(
            params={'access_token': self._token}
        )
        r = self.send_request(self._data, 'query_depart', **kwargs)
        return r

    def update_depart(self, ids, **kwargs):
        data = {'id': ids}
        data.update(kwargs)
        kwargs = dict(
            params={'access_token': self._token},
            json=data
        )
        r = self.send_request(self._data, 'update_depart', **kwargs)
        return r

    def delete_depart(self, ids):
        kwargs = dict(
            params={'access_token': self._token, 'id': ids}
        )
        r = self.send_request(self._data, 'delete_depart', **kwargs)
        return r

    def clear_env(self, data):
        for item in data:
            res = self.query_depart()
            val = jsonpath(res, f'$..department[?(@.name=="{item}")]')
            if val:
                ids = val[0]['id']
                self.delete_depart(ids)






