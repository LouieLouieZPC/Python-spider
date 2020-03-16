import re
match=re.match(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))   # 无结果，因为match是个空变量，"returning a Match object, or None if no match was found."

'''
# Output:

'''


print('----------------------------------------')


match=re.match(r'[1-9]\d{5}','100081 BIT')
if match:
    print(match.group(0))

'''
# Output:
100081
'''