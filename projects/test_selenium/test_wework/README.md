测试企业微信登录后的 admin 页面
主测功能如下：

    添加成员
    导入通讯录(文件上传)
    消息群发(文件上传、frame切换)

设计如下  (尝试通过chrome debugging mode 复用浏览器来绕过登录)
```python
# case 层
class TestAdmin:
    
    def test_add_member(self):
        pass
    
    def test_import_contact(self):
        pass
    
    def test_send_msg(self):
        pass
    
# page 层
    
class BasePage:
    """处理driver"""
    pass 


class AdminPage:
    
    def add_member(self):
        return AddMemberPage()
    
    def import_contact(self):
        
        return ImportContactPage()
    
    def send_msg(self):
        
        return SendMessagePage()
    
class AddMemberPage:
    
    def add_contact(self):
        pass
    
    
class ImportContactPage:

    def import_contact(self):
        pass


class SendMessagePage:
    def send_message(self):
        pass

....略，具体看源码

```
项目收获：

- 编码的时候一定要注意观察 HTML 代码的变化。可以一边操作，一边观察debug窗里 HTML 结构变化，很多时候
  元素找不到或者不可交互之类的错误，是因为在操作过程中 js 动态操作了 HTML结构。
  
- 一定要善于并多使用console，你在浏览器console中找不到的东西或者操作不了的东西，selenium中不可能会找到

- 每个趟坑的过程都是一次成长的机会。


