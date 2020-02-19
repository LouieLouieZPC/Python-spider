import requests
from requests.auth import HTTPBasicAuth
r=requests.get('http://www.baidu.com',auth=HTTPBasicAuth('user','user'))
print(r.status_code)
r.encoding=r.apparent_encoding
print(r.text)
print(r.headers)
print(r.request.headers)
