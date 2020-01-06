# 导包
import unittest
class Test_Add(unittest.TestCase):
    def setUp(self):
        print("开始")
    def tearDown(self):
        print("结束")
    def test01(self):
        a = 1
        b = 1
        self.assertEqual(2,a+b)
if __name__ == '__main__':
    unittest.main