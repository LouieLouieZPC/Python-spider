#!/usr/bin/env python3
#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua=UserAgent()  # 代理
kv={'user-agent':ua.random} # 随机

def getHtml(url):
        '获取HTML'
        r=requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text

def paserHtml(html):
        '''解析HTML''' 
        bs=BeautifulSoup(html,'html.parser')   
        ilt=bs.find('ul',attrs={'class':'list_con_li autoHeight'})
        ilt2=ilt.find_all('a')
        chapter_names=[]
        chapter_urls=[]
        for comic in ilt2:
                name=comic.text
                href=comic.get('href')
                chapter_names.insert(0,name)
                chapter_urls.insert(0,href)
        print(chapter_names)
        print(chapter_urls)

if __name__ == "__main__":
    url='https://www.dmzj.com/info/yaoshenji.html'
    html=getHtml(url)
    content=paserHtml(html)
    print(content)
