#!/user/bin/python
#-*-coding:utf-8-*-

import re
import requests
from fake_useragent import UserAgent




def getHtmlText(url):\
    # 部署代理
    ua=UserAgent()
    kv={'user-agent':'ua.random'}
    
    # 部署cookies
    request_cookies=requests.get

    try:
        r=requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def paserPage(ilt,html):
    print('')


def printGoodsList(ilt):
    print('')


if __name__ == "__main__":
    goods='书包'
    depth=2
    start_url='https://s.taobao.com/search?q=' + goods
    inforList=[]
    for i in range(depth):
        try:
            url=start_url+ '&s=' + str(44*i)
            html=getHtmlText(url)
            paserPage(inforList,html)
        except:  # 若某一页面解析有问题，则跳过
            continue
    printGoodsList(inforList)
