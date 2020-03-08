#!/user/bin/python
# -*-coding:utf-8-*-
import bs4
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua=UserAgent()
kv={'user-agent':ua.random}

def getHtmlText(url):
    '''
    从网络上获取大学排名网页内容
    '''
    try:
        r=requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.request.headers)
        return r.text
    except:
        return ''

def fillUnivList(ulist,html):
    '''
    提取网页内容中的信息到合适的数据结构（列表）
    '''
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag): # 查看tr是否为标签
            tds=tr('td')                   # tr('td')即tr.fina_all('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])   # 将数据输入列表中，.string指取标签的字符串

def printUnivList(ulist,num):
    '''
    利用数据结构（列表）战展示并输出结果
    '''
    print('{:^10}\t{:^6}\t{:^10}'.format('排名','学校名称','总分'))  # \t为横向制表符，^为居中对齐，10为每列的宽度

    for i in range(num):
        u=ulist[i]
        print('{:^10}\t{:^6}\t{:^10}'.format(u[0],u[1],u[2]))

if __name__ == "__main__":
    uinfo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html=getHtmlText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)  # 20 univs

