import re
i = re.search(r'py.*?n','pyanbncndnfngn')
if i:
	print(i.group(0))

pyan  #使用最小匹配操作符?，实现最小匹配