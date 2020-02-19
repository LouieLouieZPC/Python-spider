import requests
r = requests.get('https://www.12306.cn', cert=('/home/youdi/Download/**.crt', '/hone/youdi/.ssh/**.key'))
print(r.status_code)