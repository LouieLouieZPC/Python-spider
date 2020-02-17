import requests

url = 'http://httpbin.org/post'

r = requests.request('POST', url)

# 头部信息
print(r.request.headers)
print(r.request)
# 观察User-Agent