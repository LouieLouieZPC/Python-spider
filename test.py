#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 代理
ua=UserAgent()
kv={'user-agent':ua.random}    

def web_spider(url):
    '''
    爬取并解析网页的web_spider函数
    '''
    try:
        # get网页文档
        r=requests.get(url,headers=kv)
        print(r.status_code)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        demo=r.text

        # 解析
        soup=BeautifulSoup(demo,'html.parser')
        return(soup.prettify())
        
    except:
        return('Something Error!!!')

if __name__ == "__main__":
    url='https://python123.io/ws/demo.html'
    print(web_spider(url))


