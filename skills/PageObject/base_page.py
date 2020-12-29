"""
BasePage
"""


class Base:
    """简略版本"""

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_css(self, selector):
        return self.driver.find_element_by_csss_selector(selector)

    @property
    def title(self):
        return self.driver.title

    def js(self, script):
        self.driver.execute(script)

