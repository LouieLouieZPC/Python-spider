


# 爬取页面例一：
import requests
url='http://wx3.sinaimg.cn/mw600/00803BU6gy1gc36yakt6ej30hs0zktav.jpg'

try:
    r=requests.get(url)
    r.raise_for_status()
    print(r.status_code)
except:
    print('something error!!!')
