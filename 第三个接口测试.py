# 导包
import requests

url = "http://v.juhe.cn/weather/geo"
# para = {'lon': 116.39277, 'lat': 39.933748, 'key':  'bc68436b19251686cb530e6880c6cd59'}
para = {'lon': -116.39277, 'lat': 39.933748, 'key':  'bc68436b19251686cb530e6880c6cd59'}
# 发送post请求
r = requests.post(url,data=para)
# 获取json数据
res = r.json()
print(res)
print(res['error_code'])
# print(res['result']['sk'])