import requests   # 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url='https://python123.io/ws/demo.html'
ua=UserAgent()
kv={'user-agent':ua.random}

try:
    r=requests.get(url,headers=kv)
    print(r.status_code)
    r.raise_for_status()
    print(r.text)
except:
    print('Something Error')
