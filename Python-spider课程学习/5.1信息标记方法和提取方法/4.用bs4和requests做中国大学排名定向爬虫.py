#!/user/bin/python
# -*-coding:utf-8-*-
import bs4
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua=UserAgent()
kv={'user-agent':ua.random}

# https://blog.csdn.net/qq_21905401/article/details/78212780 参考
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
    for tr in soup.find('tbody').children: # 遍历所有tbody下的孩子标签
        if isinstance(tr,bs4.element.Tag): # 查看tr是否为标签
            tds=tr('td')                   # 获取所有的tr('td')即tr.fina_all('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])   # 将数据输入列表中，.string指取标签的字符串

def printUnivList(ulist,num):
    '''
    利用数据结构（列表）战展示并输出结果
    '''
    e='{0:^10}\t{1:{3}^10}\t{2:^10}'   # {3}用于填充的单个字符:使用format function 第四个变量填充，即chr(12288),此法可对中英文输出进行优化
    print(e.format('排名','学校名称','总分',chr(12288)))  # 输出第一行：\t为横向制表符，^为居中对齐，10为每列的宽度

    for i in range(num):
        u=ulist[i]
        print(e.format(u[0],u[1],u[2],chr(12288)))

if __name__ == "__main__":
    uinfo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html=getHtmlText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)  # 20 univs