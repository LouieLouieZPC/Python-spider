'''
[原案例网址](https://www.cnblogs.com/afei123/p/11234910.html)
[xpath中遇到[<Element a at 0x39a9a80>]](https://www.cnblogs.com/z-x-y/p/8260213.html)
'''

# !/user/bin/python
# -*-coding:utf-8-*-



from lxml import etree
import requests
from fake_useragent import UserAgent

url='https://music.douban.com/top250'
ua=UserAgent()
kv={"user-agent":ua.random}

def getInfo():
    r=requests.get(url,headers=kv).text
    s=etree.HTML(r)      # 创建实例
    title=s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a')[0]
    print(title.text)

if __name__ == "__main__":
    getInfo()


    





