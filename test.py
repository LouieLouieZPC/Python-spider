import requests


kv={'key1':'value1','key2':'value2'}

r=requests.request('GET','http://python123.io/ws',params=kv)   
print(r.url)


# Output:
https://python123.io/ws?key1=value1&key2=value2


