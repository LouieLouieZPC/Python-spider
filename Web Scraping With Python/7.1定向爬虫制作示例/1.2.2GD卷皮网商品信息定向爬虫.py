import requests
import re
from bs4 import BeautifulSoup

#从网络上获取背包网页内容
def getHtmlText(url):
    try:
        r =requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "123"

#提取网页内容中信息到合适的数据结构
def fillUnivList(html):
    soup = BeautifulSoup(html,"html.parser")
    divs = soup.find_all('div')
    spans = soup.find_all('span')
    for i in divs :
        if 'list-good buy' in str(i):
            tit = i.find_all('h3')[0].find_all('a')[0].string
            spans = i.find_all('span')
            if 'price-current' in str(spans[0]):
                print('商品名称: ' + tit)
                print('价格: ' + str(spans[0])[38:-7])

#主函数
def main():
    goods='书包'
    depth = 2
    url = 'http://www.juanpi.com/search?keywords=' + goods
    for i in range(1,depth+1):
        print('第' + str(i) + '页: ------------------------------------------------')
        html = getHtmlText(url)
        fillUnivList(html)
        url = 'http://www.juanpi.com/search/' + str(i+1) +'?keywords=' + goods

main()