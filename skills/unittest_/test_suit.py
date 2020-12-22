""" Test Suit"""
import unittest
from skills.unittest_.unitest_demo import TestCaseFuncs

suit = unittest.TestSuite()

# 可以添加单个测试用例
# suit.addTest(TestCaseFuncs('test_add'))
# 添加多个测试用例
# suit.addTests([TestCaseFuncs('test_add'), TestCaseFuncs('test_div')])
# # 可以通过 loader 导入测试用例
# suit.addTests(unittest.TestLoader().loadTestsFromName('unitest_demo.TestCaseFuncs'))
# suit.addTests(unittest.TestLoader().loadTestsFromNames(['unitest_demo.TestCaseFuncs']))
suit.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCaseFuncs))

if __name__ == '__main__':

    with open('TestResult.txt', 'a', encoding='utf8') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suit)

