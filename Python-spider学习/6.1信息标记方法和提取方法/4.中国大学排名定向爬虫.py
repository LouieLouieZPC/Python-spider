#!/user/bin/python
# -*-coding:utf-8-*-
import re
import bs4
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def getHtmlText(url):
    '''
    从网络上获取大学排名网页内容
    '''
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist,html):
    '''
    提取网页内容中的信息到合适的数据结构（列表）
    '''
    try:
        soup=BeautifulSoup(html,'html.parser')
        for tr in soup.find_all('tbody'):
            if isinstance(tr,bs4.element.Tag):
                tds=tr('td')                   # tr('td')即tr.fina_all('td')
                ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string]



def printUnivList(ulist,num):
    '''
    利用数据结构（列表）战展示并输出结果
    '''
    return ("Suc"+str(num))

def main():
    uinfo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html=getHtmlText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)  # 20 univs
