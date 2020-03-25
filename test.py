from urllib.request import urlopen

req=urllib.request.Request('http://placekitten.com/g/500/300')
response= urlopen(req)

cat_img=response.read()
with open('cat_500_300.jpg','wb') as f:
    f.write(cat_img)