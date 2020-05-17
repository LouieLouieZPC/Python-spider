import requests   # 获取
from bs4 import BeautifulSoup  # 解析
import traceback  # 错误捕获
import re  # 正则表达式
from fake_useragent import UserAgent  # 代理


# 获得url对应的页面内容
def getHTMLText(url,code='utf-8'):
    # 配置代理
    ua=UserAgent()
    kv={'user-agent':ua.random}
    
    try:
        r=requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding=code      # 直接赋，提高速度；若为r.encoding=r.apparent_encoding,则还要花时间分析文本内容
        return r.text
    except:
        return''
        
# 获得股票信息列表
def getStockList(lst,stockURl):
    '''
    第一个参数为存储在的列表类型，第二个参数为获得股票url的网站
    '''
    html=getHTMLText(stockURl,'GB2312')  # 获取网页内容，GB2312该网站使用的是GB2312
    soup=BeautifulSoup(html,'html.parser')  # 解析
    a=soup.findAll('a')  # 调用soup的findAll函数
    for i in a:
        try:
            href=i.attrs['href']  #获得属性href中的内容
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0])   # 调用re库的findall函数，因为它返回的是列表（联想到soup.findAll()和soup.find(),前者输出列表则需[0]，而后者输出单个结果或None，则不需要[0]），所以需要用到[0]，这是为了取出返回的值添加，不然会将空值以空列表的形式添加进去。
        except:
            continue

# 获得股票信息
def getStockInfo(lst,stockURl,fpath):
    '''
    三个参数：保存所有股票的信息列表，获得股票信息的url网站，把文件存到文件的文件路径
    '''
    count=0  # 用以计数
    for stock in lst:    # 遍历股票列表
        url=stockURl+stock+'.html'  # 修改获取股票信息的网址
        html=getHTMLText(url)  # 获取网页内容
        try:
            if html=='':   # 可能没有这个页面
                continue   # 跳过
            infoDict={}    # 采用字典的数据结构放结果
            soup=BeautifulSoup(html,'html.parser')  # 解析
            stockInfo=soup.find('div',attrs={'class':'container-sm float-left stock__main'})
            name=stockInfo.find_all(attrs={'class':'stock-name'})[0]  # 获得股票名称
            infoDict.update({'股票名称':name.text})
            keyList=stockInfo.find_all('td')
            valueList=stockInfo.find_all('span')
            for i in range(len(keyList)):
                key=keyList[i].text
                val=valueList[i].text
                infoDict[key]=val

            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
                count+=1
                print('\r当前速度：{:.2f}%').format(count*100/len(lst),end='')  # 由于print每次打印后都自动换行，若不想要换行，用\r将该功能禁掉，在该行重新打印
        except:
            traceback.print_exc()
            print('\r当前速度：{:.2f}%').format(count*100/len(lst),end='')
            continue


if __name__ == "__main__":
    stock_list_url='http://quote.eastmoney.com/stock_list.html'  # 获取股票代码列表的网站
    stock_info_url='https://xueqiu.com/S/' # 获取股票信息的网站
    output_file='D：//股票信息.text'
    slist=[]
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)