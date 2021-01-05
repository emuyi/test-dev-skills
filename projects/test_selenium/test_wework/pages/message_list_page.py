"""
消息列表页
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MessageListPage(BasePage):
    """ 定义消息列表页功能 """
    _url = 'https://work.weixin.qq.com/wework_admin/frame#messageList'

    def __init__(self):
        super().__init__(reuse=True)

    @property
    def messages(self):
        msg_elements = self._driver.find_elements(By.CSS_SELECTOR, '.msg_history_msgList_td')
        print([ele.text for ele in msg_elements])
        return ':'.join([ele.text for ele in msg_elements])

