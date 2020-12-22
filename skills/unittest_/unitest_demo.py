"""
unittest 是 python 内置的单元测试库, 也是 xUnite(如 java 的 Junit 测试框架)测试框架集合中的一员.
1. unittest 有四大核心组成部分: Test Fixture, TestCase,  TestSuit, TestRunner
从总体来看他们之间的关系, TextTestRunner 驱动 TestSuit 执行 TestCase 中的测试用例, 其中
TestCase 包含了 setUp, tearDown 等 Test Fixture.
2. 具体用法
    1.创建测试用例 TestCase
        a. 需要继承 unittest.TestCase 创建单元测试用例, 定义 test_开头的方法来测试每一个具体的功能函数
        b. 可以使用 setUp / tearDown 方法为每个 test_method 创建前置条件和后处理. 也可以用 setUpClass
        和 tearDownClass 两个类方法, 做为整个单元测试用例的前置条件和后处理.
        c. 如果需要跳过某个具体的测试用例, 可以使用 unittest.skip 装饰器
            unittest.skip(reason=msg) 直接跳过
            unittest.skipIf(condition, reason)  condition 为 True 跳过
            unittest.skipUnless(condition, reason)  condition 为 False 跳过
        d. 可以使用 unittest.main() 单独调试测试用例

    2. 添加测试用例到测试套件
        a. 由 unittest.TestSuit 生成测试套件对象
        b. 使用 addTest/ addTests 将测试用例添加到套件对象中
           主要有以下几种方法:
                addTest(TestCaseFuncs('test_add')) 添加单个测试用例
                addTests([TestCaseFuncs('test_add'), TestCaseFuncs('test_div')] 添加多个测试用例
                使用 unittest.TestLoader 导入用例, 参看demo
    3. 使用 unittest.TextTestRunner 执行用例
        1. 注意, 默认测试结果是输出到 console, 可以指定 stream 参数将结果输出到文件, 也可以指定 verbosity 参数来调整
        执行结果的详细度.
        2. 第三方库, HTMLTestRunner 以 web 的形式美化测试报告, 要注意该库不支持 python3, 需要自定制.
"""


import unittest
from skills.unittest_.funcs import *


# 继承 unittest.TestCase 创建测试用例
class TestCaseFuncs(unittest.TestCase):
    """test funcs"""

    @classmethod
    def setUpClass(cls):
        """整个测试单元的前置条件"""
        print('test env ready, test starting...')

    # def setUp(self):
    #     """每条用例的前置条件"""
    #     print('每条用例的前置条件')
    #
    # def tearDown(self):
    #     """每条用例的后置处理"""
    #     print('每条用例的后置处理')

    def test_add(self):
        """test add func"""
        self.assertEqual(add(1, 2), 3)
        self.assertNotEqual(add(2, 3), 6)

    def test_div(self):
        """test div func"""
        self.assertEqual(div(1, 2), 0.5)

    @unittest.skip(reason='目前只测试数学功能的函数,该函数先跳过')
    def test_upper(self):
        """test upper func"""
        self.assertTrue('hello'.upper())

    @classmethod
    def tearDownClass(cls):
        """整个测试单元的后置处理"""
        print('test env clean')


# 可以通过 unittest.main() 对单个用例脚本调试
# 注意这时的执行顺序是乱序的
if __name__ == '__main__':
    unittest.main()




