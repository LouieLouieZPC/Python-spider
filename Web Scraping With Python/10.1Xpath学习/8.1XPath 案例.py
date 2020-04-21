'''
[原案例网址](https://www.cnblogs.com/afei123/p/11234910.html)
[xpath中遇到[<Element a at 0x39a9a80>]](https://www.cnblogs.com/z-x-y/p/8260213.html)
'''

# !/user/bin/python
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
s
def paserPage(ilt,html):
    s=etree.HTML(html)      # 创建实例\
    trs=s.xpath('/html/body/div[3]/div[1]/div/div[1]/div/table/tr')
    for i in trs:
        title=s.xpath('./td[2]/div/a')[0]  # 获取标题
        href=s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a/@href')[0] # 获取链接地址
        score=s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/div/span[2]')[0] # 获取分数
        print(title.text,href,score.text)


def printGoodsList(ilt):




if __name__ == "__main__":
    depth=2  # 爬取深度为2，爬取3页
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
    printGoodsList()


    








//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div/p[1]

div[@id='content']/div[@class='grid-16-8 clearfix']/div[@class='article']/div[@class='indent']/table[1]/tbody/tr[@class='item']/td[2]/div[@class='pl2']/p[@class='pl']