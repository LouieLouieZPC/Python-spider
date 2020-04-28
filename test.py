import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]} # 往往字典的键都作为列标题
df = pd.DataFrame(data)
print (df)