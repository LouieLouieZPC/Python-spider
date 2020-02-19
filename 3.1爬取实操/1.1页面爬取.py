
# 爬取页面例一：
import requests
url='https://item.jd.com/100003859236.html#none'

try:
    r=requests.get(url)
    r.raise_for_status()
    print(r.status_code)
    print(r.text)
except:
    print('something error!!!')

