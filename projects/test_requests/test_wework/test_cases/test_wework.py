from projects.test_requests.test_wework.api.wework import WeWork


class TestWeWork:

    @classmethod
    def setup_class(cls):
        cls.wework = WeWork

    def test_get_token(self):
        ret = self.wework.get_access_token()
        assert ret.get('errcode') == 0
