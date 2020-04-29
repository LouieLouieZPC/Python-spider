
'''
参考CSDN网址：https://blog.csdn.net/Eastmount/article/details/79474308?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158462685019724845061474%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158462685019724845061474&biz_id=0&utm_source=distribute.pc_search_result.none-task
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import urllib2 
import re 
from bs4 import BeautifulSoup
import codecs
import csv
 
 
c = open("ycf.csv","wb") #write 写
c.write(codecs.BOM_UTF8)
writer = csv.writer(c)
writer.writerow(["短租房名称","地址","价格","评分","可住人数","人均价格"])
 
 
#爬取详细信息
def getInfo(url,fname,fprice,fscore,users):
    #通过浏览器开发者模式查看访问使用的user_agent及cookie设置访问头（headers）避免反爬虫,且每隔一段时间运行要根据开发者中的cookie更改代码中的cookie
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    cookie="mediav=%7B%22eid%22%3A%22387123%22eb7; mayi_uuid=1582009990674274976491; sid=42200298656434922.85.130.130"
    headers={"User-Agent":user_agent,"Cookie":cookie}
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    contents = response.read() 
    soup = BeautifulSoup(contents, "html.parser")
    #短租房地址
    for tag1 in soup.find_all(attrs={"class":"main"}):    
        print u'短租房地址:'
        for tag2 in tag1.find_all(attrs={"class":"desWord"}):
            address = tag2.find('p').get_text()   # .get_text()会将所有的超链接、段落、标签清除，只剩下一串不带标签的文字
            print address
    #可住人数     
        print u'可住人数:'
        for tag4 in tag1.find_all(attrs={"class":"w258"}):
            yy = tag4.find('span').get_text()     # .get_text()会将所有的超链接、段落、标签清除，只剩下一串不带标签的文字
            print yy
        fname = fname.encode("utf-8")
        address = address.encode("utf-8")
        fprice = fprice.encode("utf-8")
        fscore = fscore.encode("utf-8")
        fpeople = yy[2:3].encode("utf-8")
        ones = int(float(fprice))/int(float(fpeople))
        #存储至本地
        writer.writerow([fname,address,fprice,fscore,fpeople,ones])
    
 
#爬虫函数
def gydzf(url):
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    contents = response.read() 
    soup = BeautifulSoup(contents, "html.parser")
    for tag in soup.find_all('dd'):
    #短租房名称
        for name in tag.find_all(attrs={"class":"room-detail clearfloat"}):
            fname = name.find('p').get_text()
            print u'[短租房名称]', fname.replace('\n','').strip()
    #短租房价格
        for price in tag.find_all(attrs={"class":"moy-b"}):
            string = price.find('p').get_text()
            fprice = re.sub("[￥]+".decode("utf8"), "".decode("utf8"),string)
            fprice = fprice[0:5]
            print u'[短租房价格]', fprice.replace('\n','').strip()
    #评分及评论人数
            for score in name.find('ul'):
                fscore = name.find('ul').get_text()
            print u'[短租房评分/评论/居住人数]', fscore.replace('\n','').strip()           
   #网页链接url           
            url_dzf = tag.find(attrs={"target":"_blank"})
            urls = url_dzf.attrs['href']
            print u'[网页链接]', urls.replace('\n','').strip()
            urlss = 'http://www.mayi.com' + urls + ''
            print urlss
            getInfo(urlss,fname,fprice,fscore,user_agent)
      
#主函数
if __name__ == '__main__':    
    i = 0
    while i<33:
        print u'页码', (i+1)
        if(i==0):
            url = 'http://www.mayi.com/guiyang/?map=no'
        if(i>0):
            num = i+2 #除了第一页是空的，第二页开始按2顺序递增
            url = 'http://www.mayi.com/guiyang/' + str(num) + '/?map=no'
        gydzf(url)
        i=i+1
 
c.close()