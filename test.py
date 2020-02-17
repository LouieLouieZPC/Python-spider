import requests

url = 'http://baidu.com'

r = requests.request('GET', url)

# 头部信息
print(r.cookies)
print(type(r.cookies))
# 观察User-Agent