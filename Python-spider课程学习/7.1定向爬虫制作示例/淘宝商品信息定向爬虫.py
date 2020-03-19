#!/user/bin/python
#-*-coding:utf-8-*-

import re
import requests

def getHtmlText(url):
    print('')


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
        except:
            continue
    printGoodsList(inforList)
