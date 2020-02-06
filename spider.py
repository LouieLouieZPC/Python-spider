import requests
r=requests.get('http://baidu.com')
r.status_code
r.encoding='utf-8'
r.text()