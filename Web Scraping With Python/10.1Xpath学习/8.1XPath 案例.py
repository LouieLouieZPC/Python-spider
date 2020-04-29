'''
[原案例网址](https://www.cnblogs.com/afei123/p/11234910.html)
[xpath中遇到[<Element a at 0x39a9a80>]](https://www.cnblogs.com/z-x-y/p/8260213.html)
'''

#!/usr/bin/env python3
# -*-coding:utf-8-*-



from lxml import etree
import requests
from fake_useragent import UserAgent

ua=UserAgent()
kv={"user-agent":ua.random}


def getHtmltext(url):
    '''
    获取网页内容
    '''
    try:
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        print('Something error!!!')

def paserPage(ilt,html):
    '''
    解析清洗页面、放入数据结构中
    '''
    s=etree.HTML(html)      # 创建实例\
    trs=s.xpath('/html/body/div[3]/div[1]/div/div[1]/div/table/tr')
    for tr in trs:
        title=tr.xpath('./td[2]/div/a/text()')[0]  # 获取标题
        score=tr.xpath('./td[2]//div/div/span[2]/text()')[0].strip() # 获取分数
        numbers=tr.xpath('./td[2]/div/div/span[3]/text()')[0].strip().strip('()') # 获取评价人数
        ilt.append([title,score,numbers])

def printGoodsList(ilt):
    '''
    输出列表
    '''
    tplt='{:^8}\t{:^8}\t{:^8}\t{:^8}'
    print(tplt.format('排名','作品名称','评分','评价人数'))

    count=0
    for i in ilt:
        count+=1
        print(tplt.format(count,i[0],i[1],i[2]))

if __name__ == "__main__":
    '''
    主程序
    '''
    depth=3  # 爬取深度为3，爬取3页
    start_url="https://music.douban.com/top250?start="
    inforList=[]
    for i in range(depth):
        try:
            url=start_url+str(25*i)
        except:
            continue
        else:
            html=getHtmltext(url)
            paserPage(inforList,html)
    printGoodsList(inforList)