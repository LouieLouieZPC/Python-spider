#！/user/bin/python
#-*-coding:utf-8-*-

import re
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
url='http://www.pythonscraping.com/pages/page3.html'

ua=UserAgent()
kv={'user-agent':ua.random}


try:
    r=requests.get(url,timeout=30,headers=kv)
    print(r.status_code)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    demo=r.text
except:
    print('something is error!!!😱')
else:
    soup=BeautifulSoup(demo,'html.parser')
    print('----------------------------------------------------------------')
    images=soup.find_all('img',{'src':re.compile(r'\.\./img/gifts/img.\.jpg')})   #这里将正则表达式和find_all()函数配合使用
    for image in images:
        print(image['src'])   # 迭代打印image标签中的src属性的内容

'''
# Output:
200
----------------------------------------------------------------
../img/gifts/img1.jpg
../img/gifts/img2.jpg
../img/gifts/img3.jpg
../img/gifts/img4.jpg
../img/gifts/img6.jpg
'''