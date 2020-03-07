#!/uesr/bin/python
# -*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup

url='http://python123.io/ws/demo.html'
r = requests.get(url)
demo=r.text

