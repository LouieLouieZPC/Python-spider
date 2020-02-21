import requests
from fake_useragent import UserAgent

ua=UserAgent()
kv={'user-agent':ua.random}

url='https://ip.cn/'
ip_address={'ip':'202.101.172.35'}

try:
    r=requests.get(url,params=ip_address,headers=kv)
    print(r.status_code)
    r.raise_for_status()
    print(r.request.url)
    print(r.request.headers)
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print('Something Error')
