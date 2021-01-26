import os


class Settings:

    PROJECT_PATH = os.path.split(os.path.abspath(__file__))[0]
    DDT_PATH = os.path.join(PROJECT_PATH, 'ddt')