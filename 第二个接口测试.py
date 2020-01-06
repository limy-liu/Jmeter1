import requests
# 定义接口地址
utl = "http://v.juhe.cn/weather/uni"
# para = {"key": "bc68436b19251686cb530e6880c6cd59"}
para = {"key": "bc68436b19251686cb530e6880c6cd"}
# 发送接口请求
r = requests.get(utl,params=para)
print(r.status_code)

# 获取json数据
res = r.json()
print(res)
print(res['reason'])
print(res['error_code'])