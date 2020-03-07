#!/user/bin/python
# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError,URLError

url='http://www.pythonscraping.com/pages/page1.html'  # 准备一个网址

def getTitle(url):       # 定义函数
    '''
    getTitle function:返回网页的标题
    '''
    # 获取网页内容
    try:
        html=urlopen(url)   # 获取内容
    except HTTPError as e:  # 网页在服务器上不存在（或者获取页面的时候出现错误，返回404/500等）
        return(e)
    except URLError as e:   # 服务器不存在（URL链接写错）
        return(e)           # 这是个函数，所以做最好用return
    
    # 解析网页内容
    try:
        bs=BeautifulSoup(html.read(),'html.parser')  # 解析html内容,(其实BeautifulSoup可以直接使用urlopen返回的文件对象，无需先调用.read函数)
        title=bs.body.h1
    except AttributeError as e:     # 检查标签是否存在（若不存在会发生AttributeError错误，返回None对象）
        return None                 # 若标签不存在，返回None
    # 返回结果
    return title


title1=getTitle(url)  # 将该网页的标题赋给title1
if title1==None:      # 若等于None，则说明该标签不存在
    print('title could not be found!')
else:
    print('''This Web's heading is:\n''',title1)     # 成功得到网页的标题

    