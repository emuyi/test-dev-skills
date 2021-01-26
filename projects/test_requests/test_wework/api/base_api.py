import requests
from jsonpath import jsonpath


class BaseApi:
    """base api for steps ddt"""

    @staticmethod
    def send_request(data, api_name, **kwargs):
        request_data = dict(data.get(api_name))
        method = request_data.get('method')
        url = request_data.get('url')
        request_data.pop('method')
        request_data.pop('url')
        request_data.update(kwargs)
        r = requests.request(method, url, **request_data)
        return r.json()

    def run_steps(self, data, case_name):
        for step in data.get(case_name):
            if 'api' in step:
                r = getattr(self, 'api')
                if 'extract' in step:
                    step['extract'][0] = len(r.get('department'))
                elif 'jsonpath' in step:
                    res = jsonpath(r, step[jsonpath])
                    step['extract'][1] = res[0]['id']



