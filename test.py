import requests
from bs4 import BeautifulSoup
url="https://python123.io/ws/demo.html"
r=requests.get(url)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')

print(soup.a.next_sibling)  # 标签之间的Navigablestring也被视为一个节点
#  and


print(soup.a.next_sibling.next_sibling)
# <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>

print('-----------------------------------------------------------------------------')

print(soup.a.previous_sibling)
# Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:

print(soup.a.previous_sibling.previous_sibling)
# None

print(soup.a.parent)  # 查看父亲节点
'''
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
'''


print('-----------------------------------------------------------------------------')

print(soup.a.next_siblings)
# <generator object PageElement.next_siblings at 0x0000015DC0E05EC8>

for nsibling in soup.a.next_siblings:  # 遍历后续节点
    print(nsibling)

'''
 and
<a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>
.
'''

print(soup.a.previous_siblings)
# <generator object PageElement.previous_siblings at 0x000001EBB67B5EC8>

for psibling in soup.a.previous_sibling:
    print(psibling)

'''
P
y
t
h
o
n

i
s

a

w
o
n
d
e
r
f
u
l

g
e
n
e
r
a
l
-
p
u
r
p
o
s
e

p
r
o
g
r
a
m
m
i
n
g

l
a
n
g
u
a
g
e
.

Y
o
u

c
a
n

l
e
a
r
n

P
y
t
h
o
n

f
r
o
m

n
o
v
i
c
e

t
o

p
r
o
f
e
s
s
i
o
n
a
l

b
y

t
r
a
c
k
i
n
g

t
h
e

f
o
l
l
o
w
i
n
g

c
o
u
r
s
e
s
:
'''