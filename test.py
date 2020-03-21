#！/user/bin/python
#-*-coding:utf-8-*-

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

ua=UserAgent()
kv={'user-agent':ua.random}

url='http://www.pythonscraping.com/pages/page3.html'

r=requests.get(url,timeout=30,headers=kv)
r.raise_for_status()
r.encoding=r.apparent_encoding


soup=BeautifulSoup(r.text,'html.parser')



for child in soup.find('table',{'id':'giftList'}).children:  # 得到第一项子标签
    print(child) 

for siblig in soup.find_all('table',{'id':'giftList'}).tr.next_sibligs:
    print(siblig)


print(soup.find('img',{'scr':'../img/gifts/img1.jpg'}).parent.previous_siblig.get_text())


