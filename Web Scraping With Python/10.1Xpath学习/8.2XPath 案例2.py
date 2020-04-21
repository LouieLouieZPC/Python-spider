from lxml import etree
import requests
import json
import re

def getUrl():
   '''
   得到url
   '''
   # 爬取深度10，即爬取11页
   for i in range(10):
      url = 'https://music.douban.com/top250?start={}'.format(i*25)
      spyder(url)

def spyder(url):
    #模拟浏览器
    kv = {'user-agent':'Mozilla/5.0'}
    # 获取html内容
    html = requests.get(url , headers = kv).text
    # 解析
    s = etree.HTML(html)

    trs = s.xpath('/html/body/div[3]/div[1]/div/div[1]/div/table/tr')

   # 循环
    for tr in trs:
        href = tr.xpath('./td[2]/div/a/@href')[0]
        title = tr.xpath('./td[2]/div/a/text()')[0].strip()  # .strip()默认为删除字符串前后的空白字符
        score = tr.xpath('./td[2]/div/div/span[2]/text()')[0].strip() # .strip()默认为删除字符串前后的空白字符
        numbers = tr.xpath('./td[2]/div/div/span[3]/text()')[0].strip().replace(" ","").replace("\n","")  # replace(" ","")和.replace("\n","")将字符串中的空格和换行符删除
        img = tr.xpath('./td[1]/a/img/@src')[0].strip()
        
        # 放入列表存储结构中
        items = [href,title,score,numbers,img]
        # 
        with open('temp.txt','a',encoding = 'utf-8') as f:
            f.write(json.dumps(items,ensure_ascii=False) + '\n')


if '_main_':
    getUrl()