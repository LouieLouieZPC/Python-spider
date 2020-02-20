import requests
from fake_useragent import UserAgent
ua=UserAgent()     # 类创建实例对象
kv={'user-agent':ua.random}       # 创建字典，制作请求头，.random属性
url='https://www.runoob.com/wp-content/uploads/2019/02/xcc8bae8c5bb5b3f01a9f8b37a24dd25295e7b66d.jpg'   # 请求网络图片的地址
path=r'D:\01.Software\GitHub\GitHub Repository\Python-spider\3.2案例\abc.jpg'   # 保存路径

try:
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    print(r.status_code) # 查看响应状态信息，200
    print(r.request.headers)  # 查看请求头信息
    
except:
    print('Something Error')
else:
    with open(path,'wb') as f:     # 打开，写入二进制文件
        f.write(r.content)    # r.content为二进制格式


