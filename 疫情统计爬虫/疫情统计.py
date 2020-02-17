import requests
import re
import pandas as pd
### 发送请求，获取信息
url = 'https://3g.dxy.cn/newh5/view/pneumonia?scene=2&clicktime=1579582238&enterid=1579582238&from=timeline&isappinstalled=0'
res = requests.get(url)
res.encoding = 'utf-8'
pat0 = re.compile('window.getAreaStat = ([\s\S]*?)</script>')
data_list = pat0.findall(res.text)
data = data_list[0].replace('}catch(e){}','')
data = eval(data)
### 解析数据，提取数据

provinceShortNames = []
currentConfirmedCounts= []
confirmedCounts = []
curedCounts = []
deadCounts = []

for i in data:
    provinceShortNames.append(i['provinceShortName'])
    currentConfirmedCounts.append(i['currentConfirmedCount'])
    confirmedCounts.append(i['confirmedCount'])
    curedCounts.append(i['curedCount'])
    deadCounts.append(i['deadCount'])
df = pd.DataFrame()
df['地区'] = provinceShortNames
df['现存确诊']= currentConfirmedCounts
df['累计确诊'] = confirmedCounts
df['死亡'] = deadCounts
df['治愈'] = curedCounts
df.T  
### 保存数据

#记录下爬取的日期，该日期将放入Excel文件的名称中
import time 
date = time.strftime('%Y%m%d')
# 保存成Excel表格
df.to_excel(date+'疫情数据.xlsx')