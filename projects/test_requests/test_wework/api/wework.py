import requests

from projects.test_requests.test_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    """wework apis, such as get access token"""

    _corpid = 'xxx'
    _token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    _secret = 'xxx'

    @classmethod
    def get_access_token(cls, secret=_secret):
        r = requests.get(cls._token_url, params=dict(corpid=cls._corpid, corpsecret=secret))
        return r.json()

    @classmethod
    def get_token(cls, secret):
        r = cls.get_access_token(secret)
        return r.get('access_token')

