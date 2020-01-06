# # 导包
# import requests
#
# # 给接口地址定义变量名称
# # url = "http://v.juhe.cn/weather/index"
# # para = {"cityname": "北京", "key": "221ec2c9d854d2859310ea808cb760fd"}
# #
# # # 发送请求
# # r = requests.get(url, params=para)
# # print(r.status_code)
#
# # 获取json数据
# # res = r.json()
# # print(res["reason"])
# # print(res["result"])
# # print(res["result"]["sk"])
# # print(res["result"]["sk"]["temp"])
#
#
# url = "http://v.juhe.cn/weather/index"
# para = {"cityname": "北京", "key": "221ec2c9d854d2859310ea808cb760f"}
# r = requests.get(url,params=para)
# print(r.status_code)
#
# res = r.json()
# print(res)
# print(res['error_code'])


# import requests
# url = "http://v.juhe.cn/weather/index"
# para = {'cityname' : '上海', 'key' : 'bc68436b19251686cb530e6880c6cd59'}
# r = requests.get(url, params=para)
# print(r.json())

# import requests
# url = "http://v.juhe.cn/weather/uni"
# para = {'key' : 'bc68436b19251686cb530e6880c6cd59'}
# r = requests.get(url, params=para)
# print(r.json())

import requests
url = "http://v.juhe.cn/weather/geo"
para = {"lon": "116.39277", "lat": "39.933748", "key": "bc68436b19251686cb530e6880c6cd59"}
r = requests.post(url, data=para)
print(r.json())