import os


class Settings:

    PROJECT_PATH = os.path.split(os.path.abspath(__file__))[0]
    LOG_PATH = os.path.join(PROJECT_PATH, 'log')
    DATA_PATH = os.path.join(PROJECT_PATH, 'data')
    CASE_PATH = os.path.join(PROJECT_PATH, 'test_cases')
    REPORT_PATH = os.path.join(PROJECT_PATH, 'report')
