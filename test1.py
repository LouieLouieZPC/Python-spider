
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
    df = pd.read_html(tb, encoding='utf-8', header=0)[0]
    # 转换成列表嵌套字典的格式
    result = list(df.T.to_dict().values())
    # 保存为csv格式
    df.to_csv(path_or_buf='D:\01.Software\GitHub\GitHub Repository\Python-spider\1.1Requests库学习\疫情.csv', index=False)
    print(result)


if __name__ == '__main__':
    main()