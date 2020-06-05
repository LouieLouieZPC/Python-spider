#!/usr/bin/env python3
#-*-coding:utf-8-*-

import requests
import os
import re
from bs4 import BeautifulSoup
from contextlib import closing
from tqdm import tqdm    # Tqdm 是 Python 进度条库，可以在 Python 长循环中添加一个进度提示信息用法：tqdm(iterator)
import time
from fake_useragent import UserAgent

"""
    Author:
        Jack Cui
    Wechat:
        https://mp.weixin.qq.com/s/OCWwRVDFNslIuKyiCVUoTA
"""

ua=UserAgent()
kv={'user-agent':ua.random}

# 创建保存目录
save_dir = '妖神记'
if save_dir not in os.listdir('./'):
    os.mkdir(save_dir)
    
target_url = "https://www.dmzj.com/info/yaoshenji.html"
 
# 获取动漫章节链接和章节名
r = requests.get(url = target_url,headers=kv)               # 获取
bs = BeautifulSoup(r.text, 'lxml')               # 解析
list_con_li = bs.find('ul', class_="list_con_li")
cartoon_list = list_con_li.find_all('a')
chapter_names = []                # 创建空列表放章节名
chapter_urls = []                 # 创建空列表放链接名
for cartoon in cartoon_list:
    href = cartoon.get('href')
    name = cartoon.text
    chapter_names.insert(0, name)  # 放入章节名
    chapter_urls.insert(0, href)   # 放入章节链接
 
# 下载漫画 
for i, url in enumerate(tqdm(chapter_urls)):    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据下标和数据，一般用在 for 循环当中。
    download_header = {
        'Referer': url
    }
    name = chapter_names[i]
    # 去掉.
    while '.' in name:
        name = name.replace('.', '')
    chapter_save_dir = os.path.join(save_dir, name)   # 章节保存路径; os.path.join()把两个路径合成一个,两者之间自动加入'/'
    if name not in os.listdir(save_dir):
        os.mkdir(chapter_save_dir)               # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
        r = requests.get(url = url)              # 获取
        html = BeautifulSoup(r.text, 'lxml')     # 解析
        script_info = html.script                # 选中script标签
        pics = re.findall('\d{13,14}', str(script_info))   
        for j, pic in enumerate(pics):   
            if len(pic) == 13:                   # 若值长度为13
                pics[j] = pic + '0'              # 给所有值末尾补位'0'
        pics = sorted(pics, key=lambda x:int(x)) # 排序
        chapterpic_hou = re.findall('\|(\d{5})\|', str(script_info))[0]
        chapterpic_qian = re.findall('\|(\d{4})\|', str(script_info))[0]
        for idx, pic in enumerate(pics):    # idx为下标；而pic为数字值
            if pic[-1] == '0':
                url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic[:-1] + '.jpg'
            else:
                url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.jpg'
            pic_name = '%03d.jpg' % (idx + 1)   # %nd：n代表的是列宽长度；%0nd：0(数字零)代表的是不足n位长度的左补齐0;d代表的是整型
            pic_save_path = os.path.join(chapter_save_dir, pic_name)   # 在某个目录下创建一个新目录/文件，首先把新目录的完整路径表示出来:
            with closing(requests.get(url, headers = download_header, stream = True)) as response:  
                chunk_size = 1024  
                content_size = int(response.headers['content-length'])  
                if response.status_code == 200:   # 连接成功
                    with open(pic_save_path, "wb") as file:    # 打开本地文件夹路径pic_save_path，以二进制写入，命名为file
                        for data in response.iter_content(chunk_size=chunk_size):     # 当流下载时，用Response.iter_content或许更方便些。requests.get(url)默认是下载在内存中的，下载完成才存到硬盘上，可以用Response.iter_content　来边下载边存硬盘;chunk_size 可以自由调整为可以更好地适合您的用例的数字 ;https://www.cnblogs.com/chjbbs/p/8250588.html
                            file.write(data)  
                else:
                    print('链接异常')
        time.sleep(10)