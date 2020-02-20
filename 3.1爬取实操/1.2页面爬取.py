
#  爬取页面例二：
import requests
from fake_useragent import UserAgent
ua=UserAgent()     # 类创建实例对象
kv={'user-agent':ua.random}       # 创建字典，制作请求头，.random属性
url='https://www.bilibili.com/video/av9784617?p=16'   # 请求网址


try:
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    print(r.status_code) # 查看响应状态信息
    print(r.request.headers)  # 查看请求头信息
    print(r.headers)          # 查看响应头信息
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print('Something Error')
