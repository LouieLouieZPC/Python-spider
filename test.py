from bs4 import BeautifulSoup
newsoup=BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>",'html.parser')
print(newsoup.b.string)
print(type(newsoup.b.string))
print(newsoup.p.string)
print(type(newsoup.p.string))