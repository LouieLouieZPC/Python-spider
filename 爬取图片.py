#!/usr/bin/env python3
#-*-coding:utf-8-*-

import re
import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua=UserAgent()
kv={'user-agent':ua.random}

url='https://www.dmzj.com/view/yaoshenji/41917.html#@page=1'

r=requests.get(url,timeout=30,headers=url)
html=BeautifulSoup(r.text,'lxml')
script_info=html.script
chapterpic_hou=re.findall('')