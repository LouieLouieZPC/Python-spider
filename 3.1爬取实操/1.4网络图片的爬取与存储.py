import requests
url='http://www.baidu.com/s'
kv={'wd':'你好'}
r=requests.get(url,params=kv)
print(r.status_code)
print(r.request.url)
