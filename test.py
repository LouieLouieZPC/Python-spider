#!/usr/bin/env python3
#-*-coding:utf-8-*-

import pandas as pd

df=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
print(df)
print('----------------------------------------')
df1=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
df=df.append(df1)
print(df)