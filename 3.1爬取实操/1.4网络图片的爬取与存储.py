import requests
import os

path='D:\01.Software\GitHub\GitHub Repository\Python-spider\3.2案例'
url='http://www.runoob.com/wp-content/uploads/2019/02/xcc8bae8c5bb5b3f01a9f8b37a24dd25295e7b66d.jpg'

r=requests.get(url)


with open(path,'wb') as f:
    f.write(r.content)

