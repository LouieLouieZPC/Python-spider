#！/user/bin/python
#-*-coding:utf-8-*-

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

ua=UserAgent()
kv={'user-agent':ua.random}




r=requests.get(url,timeout=30,headers=kv)
r.raise_for_status()
r.encoding=r.apparent_encoding


    bs=BeautifulSoup(html,'html.parser')

    for child in bs.find('table',{'id':'giftList'}).children:  # 得到第一项子标签
        print(child
    
    for siblig in bs.find('table',{'id':'giftList'}).tr.next_sibligs:
        return siblig
    
    return (bs.find('img',{'scr':'../img/gifts/img1.jpg'}).parent.previous_siblig.get_text())


if __name__ == "__main__":
    url='http://www.pythonscraping.com/pages/page3.html'
    html=get_htmltext(url)
    print(parser_page(html))
