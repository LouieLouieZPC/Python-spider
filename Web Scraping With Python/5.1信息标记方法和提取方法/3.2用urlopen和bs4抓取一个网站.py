#!/user/bin/python
# -*-coding:utf-8-*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

url='http://www.pythonscraping.com/pages/warandpeace.html'

# 获取html
html=urlopen(url)
print(html.status)
# 解析html
soup=BeautifulSoup(html.read(),'html.parser')
# 查找遍历
namelist=soup.find_all('span',{'class':'green'})   # 找到所有符合条件的html文档内容给namelist
for name in namelist:          # 遍历namelist
    print(name.get_text())     # .get_text()会将所有的超链接、段落、标签清除，只剩下一串不带标签的文字

namelist1=soup.find_all(text='the prince')  # 用标签的text文本内容去匹配
print(len(namelist1))  # 打印出匹配到'the prince'内容的标签数量