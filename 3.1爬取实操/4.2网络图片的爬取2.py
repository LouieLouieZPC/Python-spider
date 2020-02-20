import requests
import os
from fake_useragent import UserAgent

# 网址
url='http//wx3.sinaimg.cn/mw600/00803BU6gy1gc36yakt6ej30hs0zktav.jpg'
# 伪装头部
ua=UserAgent()
kv={'user-agent':ua.random}

# 用图片原来的名字存储路径（在本地）
root=r'D:\01.Software\GitHub\GitHub Repository\Python-spider\3.2案例'
path=root+url.split('/')[-1]


try:
    if not os.path.exists(root):
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
    print('File saved failed!')