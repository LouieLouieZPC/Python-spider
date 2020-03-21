#！/user/bin/python
#-*-coding:utf-8-*-

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

ua=UserAgent()
kv={'user-agent':ua.random}


def get_htmltext(url):
    try:
        r=requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
    except:
        print('Something is Error😱')
    return r.text

def parser_page(html):
    soup=BeautifulSoup(html,'html.parser')
    return soup

def get_children(bs):
    for child in bs.find('table',{'id':'giftList'}).children:  # 得到第一项子标签
        return child

def get_sibling(bs):
    for siblig in bs.find('table',{'id':'giftList'}).tr.next_sibligs:
        return siblig

def get_parents(bs):
    return (bs.find('img',{'scr':'../img/gifts/img1.jpg'}).parent.previous_siblig.get_text())

if __name__ == "__main__":
    url='http://www.pythonscraping.com/pages/page3.html'
    html=get_htmltext(url)

    bs=parser_page(html)
    
    print('----------------------------------------------------------------------------')
    print(get_children(bs))
    print('----------------------------------------------------------------------------')
    print(get_sibling(bs))
    print('----------------------------------------------------------------------------')
    print(get_parents(bs))
