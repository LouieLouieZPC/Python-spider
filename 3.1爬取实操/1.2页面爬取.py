
#  爬取页面例二：
import requests
from fake_useragent import UserAgent
ua=UserAgent()     # 类创建实例对象
kv={'user-agent':ua.random}       # 创建字典，制作请求头，.random属性
url='https://www.amazon.cn/dp/B00QWUY472/ref=sr_1_10?_encoding=UTF8&dchild=1&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_p=b7e2e0f4-2cc5-4ac8-830d-2fc357038206&pf_rd_r=CQD1VEBRYXMEE17FN0WQ&pf_rd_s=Tcg-slide-di&pf_rd_t=36701&qid=1582118133&s=jewelry&sr=1-10'   # 请求网址


try:
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    print(r.status_code) # 查看响应状态信息
    print(r.request.headers)  # 查看请求头信息
    print(r.headers)          # 查看响应头信息
    print(r.text)
except:
    print('Something Error')