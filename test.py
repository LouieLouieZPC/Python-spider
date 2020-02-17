import requests
from requests.exceptions import ReadTimeout,ConnectTimeout,RequestException


try:
    response=requests.get('http://httpbin.org/get',timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')    # 超时异常
except ConnectTimeout:
    print('Connection error')    # 连接异常
except RequestException:
    print('Error')      # 请求异常