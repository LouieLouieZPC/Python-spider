#!/user/bin/python
# -*-coding:utf-8-*-

from urllib.request import urlopen
from urllib.error import HTTPError,URLError

url='https://python123.io/ws/demo.html'
try:
    html=urlopen(url)
except HTTPError as e:  # 网页在服务器上不存在（或者获取页面的时候出现错误，返回404/500等）
    print(e)
except URLError as e:   # 服务器不存在（URL链接写错）
    print(e)
else:
    print('It worked!')