import pytest
import time
from settings import Settings as ST


def run():
    current_time = time.strftime("%Y%m%d%H%M%S")
    # pytest.main([
    #     "-s", "-v", ST.CASE_PATH,
    #     f"--alluredir={ST.REPORT_PATH}/report_{current_time}"
    # ])

    pytest.main([
        "-s", "-v", "-k", 'login_by_passwd',
        f"--alluredir={ST.REPORT_PATH}/report_{current_time}"
    ])


if __name__ == '__main__':
    run()


