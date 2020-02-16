import requests

r=requests.post('http://httpbin.org/post',data='ABC')   # 向URL POST一个字符串，自动编码为data（数据）
print(r.text)


# Output:

