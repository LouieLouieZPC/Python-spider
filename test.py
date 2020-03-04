import requests
from bs4 import BeautifulSoup
url="https://python123.io/ws/demo.html"
r=requests.get(url)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print(soup.head)     # 查看head标签
# <head><title>This is a python demo page</title></head>
print(soup.head.contents)     # 查看head标签的孩子节点  
# [<title>This is a python demo page</title>]