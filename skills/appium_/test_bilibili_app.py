"""
testing bilibili app （PO形式） 这里是简写，不做文件上的区分
"""
import time
from poium import Page, NewPageElement
from app_config import app_caps, driver


class BilibiliPage(Page):
    widget_agree = NewPageElement(id_='tv.danmaku.bili:id/agree')
    widget_login = NewPageElement(id_='tv.danmaku.bili:id/avatar')
    widget_passwd_login = NewPageElement(id_='android:id/button1')
    widget_username = NewPageElement(id_='tv.danmaku.bili:id/username')
    widget_passwd = NewPageElement(id_='tv.danmaku.bili:id/userpwd')
    widget_login_btn = NewPageElement(id_='tv.danmaku.bili:id/btn_login')


def test_wrong_username_passwd(driver):
    bp = BilibiliPage(driver)
    time.sleep(5)
    bp.widget_agree.click()
    bp.widget_login.click()
    bp.widget_passwd_login.click()
    bp.widget_username = 'xxx'
    bp.widget_passwd = 'yyy'
    bp.widget_login_btn.click()
    # WEBVIEW_tv.danmaku.bili:web 验证







