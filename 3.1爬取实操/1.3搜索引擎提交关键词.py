# -*-coding:utf-8-*-

import requests
from fake_useragent import UserAgent
ua=UserAgent()
url='http://www.so.com/s'
kv={'user-agent':ua.random}
ask={'q':'python'}

try:
    r=requests.get(url,params=ask,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.status_code)
    print(r.request.url)             # 查看请求request的url
    print(r.request.headers)
    print(r.text)

except:
    print('Something Error!!!')
