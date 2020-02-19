import requests
from requests.exceptions import ReadTimeout

try:
    r=requests.get('HTTP://www.baidu.com',timeout=0.01)
    print(r.headers)
except ReadTimeout:
    print('request is timeout!!!')