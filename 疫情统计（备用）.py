import time, json, requests
import csv


#文件名称
ExcelName = '2.3疫情日报.csv'

#当前日期时间戳
number = format(time.time() * 100, '.0f')

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%s' % number
datas = json.loads(requests.get(url=url).json()['data'])

print('更新时间：' + datas['lastUpdateTime'])
#写入更新时间
with open(ExcelName, 'a', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['更新时间：' + datas['lastUpdateTime']])

for contry in datas['areaTree']:
    if contry['name'] == '中国':
        for province in contry['children']:
            print(province['name'])
            #写入省份名称
            with open(ExcelName, 'a', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([province['name']])
            for city in province['children']:
                print(city['name'], '确诊:' + str(city['total']['confirm']), '死亡:' + str(city['total']['dead']), '治愈:' + str(city['total']['heal']))
                # 写入市的名称，确诊、死亡、治愈的人数
                with open(ExcelName, 'a', encoding='utf-8', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([city['name'], '确诊:' + str(city['total']['confirm']), '死亡:' + str(city['total']['dead']), '治愈:' + str(city['total']['heal'])])