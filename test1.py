import pandas as pd
import requests
from fake_useragent import UserAgent
import random
from lxml import etree

'''请求头函数'''

def agent():
    ua = UserAgent()
    # 随机选择chrome、ie、firefox请求头
    useragent = random.choice([ua.chrome, ua.ie, ua.firefox])
    headers = {
        'User-Agent': useragent,
        'Referer': 'https: // cn.bing.com /'
    }
    return headers


'''解析网页数据'''

def parse_html(url):
    try:
        resp = requests.get(url, headers=agent())
        # 将编码方式设置为从内容中分析出的响应内容编码方式
        resp.encoding = resp.apparent_encoding
        if resp.status_code == 200:
            tree = etree.HTML(resp.text)
            # 定位获取表格信息
            tb = tree.xpath('//script[@id="getAreaStat"]')
            # 将byte类型解码为str类型
            tb = etree.tostring(tb[0], encoding='utf8').decode()
            return tb
        else:
            print('爬取失败')
    except Exception as e:
        print(e)

def main():
    url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    tb = parse_html(url)
    # 解析表格数据
    df = p