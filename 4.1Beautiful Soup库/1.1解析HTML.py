'''
使用 Beautiful Soup 解析 html 文件:


#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import re
 
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
#获取所有的链接
links = soup.find_all('a')
print "所有的链接"
for link in links:
    print link.name,link['href'],link.get_text()
 
print "获取特定的URL地址"
link_node = soup.find('a',href="http://example.com/elsie")
print link_node.name,link_node['href'],link_node['class'],link_node.get_text()
 
print "正则表达式匹配"
link_node = soup.find('a',href=re.compile(r"ti"))
print link_node.name,link_node['href'],link_node['class'],link_node.get_text()
 
print "获取P段落的文字"
p_node = soup.find('p',class_='story')
print p_node.name,p_node['class'],p_node.get_text()


'''





import requests   # 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url='https://python123.io/ws/demo.html'
ua=UserAgent()
kv={'user-agent':ua.random}

try:
    r=requests.get(url,headers=kv)
    print(r.status_code)
    r.raise_for_status()
    print(r.text)     # 打印出页面的源代码(内容)
    demo=r.text       # 将r.text赋值给变量
    soup=BeautifulSoup(demo,'html.parser')     # 创建BeautifulSoup类的实例，输入两个变量：
except:
    print('Something Error')
