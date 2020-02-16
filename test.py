import requests


kv={'key1':'value1','key2':'value2'}

r=requests.request('http://python123.io/ws',params=kv)   
print(r.text)


# Output:

