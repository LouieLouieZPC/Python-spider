import requests
import os
from fake_useragent import UserAgent

# 网址
url='http://wx3.sinaimg.cn/mw600/00803BU6gy1gc36yakt6ej30hs0zktav.jpg'  # 图片地址
# 伪装头部
ua=UserAgent()
kv={'user-agent':ua.random}

# 用图片原来的名字存储路径（在本地）
root=r'D:\01.Software\GitHub\GitHub Repository\Python-spider\3.2案例'    # 定义根目录
path=root+url.split('/')[-1]     # 把文件保存路径标识为根目录+以反斜杠分割的最后一部分


def get_photo():
    try:
        if not os.path.exists(root):      # 判断根目录是否存在
            os.mkdir(root)
        if not os.path.exists(path):
            r=requests.get(url,headers=kv)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print('File saved successfully!')
        print('The file already exists!')
    except:
        print('Crawl failed!')
    return 'get_photo OK!'

print(get_photo())   # 运行函数