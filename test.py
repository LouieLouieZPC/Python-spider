import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4']) # 注：index参数为每行分配一个索引。索引的长度应等于数组的长度
print (df)