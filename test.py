import requests

r= requests.get('https://www.baidu.com')
print(r.status_code)
print(r.apparent_encoding)
r.encoding=r.apparent_encoding
print(r.text)