import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 代理
ua=UserAgent()
kv={'user-agent',ua.random}    

def web_spider(url):
    '''
    爬取并解析网页的web_spider函数
    '''
    try:
        # get网页文档
        r=requests.get(url,headers=kv)
        print(r.status_codes)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        demo=r.text
        
        # 解析


    except:
        print('Something Error!!!')




