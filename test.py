import re # 正则表达式库
from bs4 import BeautifulSoup
import  requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
# 查找demo里的a标签里的href的内容
for link in soup.find_all('a'):
    print(link.get('href'))
# 输出所有a和b标签在列表中
print(soup.find_all(['a','b']))
# <tag>.find_all(True)，结果将是当前所有标签信息   
for tag in soup.find_all(True):
    print(tag.name)
# 用正则表达式查找demo里以b开头的所有标签
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
# 查找demo里的p标签里的course的内容
print(soup.find_all('p','course'))
# 查找demo里的id属性=link1的元素,如果link1没有，将输出空
print(soup.find_all(id='link1'))
# 用正则表达式来输出link字符串(以link开头)
print(soup.find_all(id=re.compile('link')))
#　recursive是否对子孙全部检索，默认为True
print(soup.find_all('a',recursive=False))
# 检索Basic Python字符串
print(soup.find_all(string = 'Basic Python'))
# 用正则表达式检索含有python的所有字符串
print(soup.find_all(string = re.compile('python')))