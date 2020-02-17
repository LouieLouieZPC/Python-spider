
```python
import requests


url='http://httpbin.org/get'

r=requests.get(url)
print(r.status_code)
x=r.headers.items()
for k,v in x:
    print('{}:{}'.format(k,v))


# Output:
200
Date:Mon, 17 Feb 2020 11:29:51 GMT
Content-Type:application/json
Content-Length:306
Connection:keep-alive
Server:gunicorn/19.9.0
Access-Control-Allow-Origin:*

```