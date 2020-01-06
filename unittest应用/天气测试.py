import requests
import unittest

class Test_Tq(unittest.TestCase):
    def setUp(self):
        print("开始")
    def tearDown(self):
        print("结束")
    def test01(self):
        # 接口地址
        url = "http://v.juhe.cn/weather/index"
        # 构造数据
        para = {"cityname":"苏州", "key":"bc68436b19251686cb530e6880c6cd59"}
        res = requests.get(url,params=para)
        r = res.json()
        # print(r)
        self.assertEqual(r['reason'],'successed!')
if __name__ == '__main__':
    unittest.main()
