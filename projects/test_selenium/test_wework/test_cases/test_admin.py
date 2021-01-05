"""
测试企业微信web版admin页面
"""
import time
from pages.admin_page import AdminPage

msg_info = (
    '公告',  # 注意 公告的页面和普通app的编辑页面不一样，这里选择公告(东西多)
    'bobby',
    '快递',
    'bobby来前台收快递',
    r'C:\Users\MUYI\Desktop\test_wework\通讯录批量导入模板.xlsx',
    r'C:\Users\MUYI\Desktop\test_wework\test.png',
    '快递!',
    'ellen'
)


class TestAdmin:

    def setup_method(self):
        self.admin_page = AdminPage()

    def test_add_member(self):
        """测试管理员页面添加成员功能"""
        # 1. save_and_add  todo 这块的 assert 按理说应该通过弹窗 text 判断，但比较难确定是弹窗还是其他的js动态效果
        # add_member_page = self.admin_page.add_member().save_and_add('bill3', 'bill3', '12345678114', '2')
        # 2. save
        add_member_page = self.admin_page.add_member().save('bill4', 'bill4', '12345678115', '2')
        assert 'bill4' in add_member_page.member_info
        # 3. cancel
        # self.admin_page.add_member().cancel()

    def test_import_contact(self):
        """测试管理员页面导入通讯录功能"""
        contact_page = self.admin_page.import_contact().upload_contact_file(
            r'C:\Users\MUYI\Desktop\test_wework\通讯录批量导入模板.xlsx')
        assert '张三3' in contact_page.member_info  # todo 这块应当读xlsx文件比对数据

    def test_send_message(self):
        """测试管理员页面消息群发功能"""
        msg_list = self.admin_page.send_message().send(*msg_info)
        assert '快递' in msg_list.messages

    def teardown_method(self):
        time.sleep(2)
        self.admin_page.quit()
