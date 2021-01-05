import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.message_list_page import MessageListPage


class SendMessagePage(BasePage):
    """定义发消息页面功能"""

    def create_message(self, app, to, title, contents, attach_file, img_path, summary, author):
        # 选择应用
        self._driver.find_element(By.LINK_TEXT, '选择需要发消息的应用').click()
        # TODO 1 元素不可交互 ：没找对元素
        app_locator = (By.CSS_SELECTOR, 'div[data-name="{}"]'.format(app))
        self._driver.find_element(*app_locator).click()
        self._driver.find_element(By.LINK_TEXT, '确定').click()
        # 选择发送范围
        # TODO 2 元素不可交互: 感觉是企业微信的前端设计问题，标签中明明只有一个，找出来有四个，其中三个还是隐藏
        self._driver.find_element(By.LINK_TEXT, '选择发送范围').click()
        search_input_locator = (By.CSS_SELECTOR, '.ww_searchInput > input')
        WebDriverWait(self._driver, 2).until(EC.visibility_of_element_located(search_input_locator))
        self._driver.find_elements(*search_input_locator)[-1].send_keys(to)  # 只有最后一个在console窗中能被选中
        self._driver.find_element(By.CSS_SELECTOR, '#search_member_list_title+ul>li:nth-child(1)').click()  # 取搜索到第一个结果
        self._driver.find_element(By.LINK_TEXT, '确认').click()
        # 编辑标题
        self._driver.find_element(By.CSS_SELECTOR, '.ww_editorTitle').send_keys(title)
        # 编辑内容
        frame_locator = (By.CSS_SELECTOR, '#ueditor_0')
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(frame_locator))
        iframe = self._driver.find_element(*frame_locator)
        self._driver.switch_to.frame(iframe)
        # # TODO 3 iframe 如何填充：直接实现 js 进行填充，它里面有个伪类选择器来加样式，所以填充的时候会有样式，但不影响数据
        contents_script = 'document.querySelector(".mpnews > p").innerText="{}"'.format(contents)
        self._driver.execute_script(contents_script)
        self._driver.switch_to.default_content()
        # # 添加附件
        self._driver.find_element(By.CSS_SELECTOR, '.js_announce_uploadFile').send_keys(attach_file)
        time.sleep(5)  # 这里强制等待文件上传，主要是因为文件未上传完整，不让发送
        # TODO 4 element click intercepted：和问题二一样的原因
        # 添加图片
        self._driver.find_elements(By.CSS_SELECTOR, '.js_announcement_cover_editBtn')[0].click()
        self._driver.find_element(By.CSS_SELECTOR, 'input[class="ww_fileInput js_file"]').send_keys(img_path)
        self._driver.find_element(By.LINK_TEXT, '确定').click()
        # 添加摘要 TODO 5 textarea: 1.textarea 是动态显示的，2. 和问题二四一样
        self._driver.find_element(By.CSS_SELECTOR, '.msg_edit_infoItem_textWord').click()
        self._driver.find_elements(By.TAG_NAME, 'textarea')[-1].send_keys(summary)
        # 添加作者
        self._driver.find_element(By.CSS_SELECTOR, '.js_amrd_sendName').send_keys(author)

    def send(self, app, to, title, contents, attach_file, img_path, summary, author):
        self.create_message(app, to, title, contents, attach_file, img_path, summary, author)
        self._driver.find_element(By.CSS_SELECTOR, '.js_save_send').click()
        self._driver.find_element(By.LINK_TEXT, '确定').click()
        return MessageListPage()


