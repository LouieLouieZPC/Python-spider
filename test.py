#!/usr/bin/env python3
#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
#BeautifulSoup是一个类
r = requests.get('http://python123.io/ws/demo.html')

# print(r.text)
demo = r.text    # 获取内容
#解析demo的解释器
soup = BeautifulSoup(demo,'html.parser')

for link in soup.find_all('a'):   # 搜索所有的a标签
    print(link.get('href'))       # 提取href后的链接内容


# Output：
'''
http://www.icourse163.org/course/BIT-268001
http://www.icourse163.org/course/BIT-1001870001
'''