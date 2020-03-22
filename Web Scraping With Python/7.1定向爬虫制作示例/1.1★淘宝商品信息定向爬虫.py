#!/user/bin/python
#-*-coding:utf-8-*-

import re
import requests
from fake_useragent import UserAgent


def getHtmlText(url):
    # 部署代理
    ua=UserAgent()
    kv={'user-agent':'ua.random'}
    
    # 部署cookies
    ck={'cookie':'t=8d41af525be6d60e1d40814674d8820f; cna=9dnxFsgkIAcCAbeAITjWCrnN; _m_h5_tk=2b59e81209230ce0623bd4421057f1fd_1584595870333; _m_h5_tk_enc=4ef52ed9a0b7cd7127e4e0480946ff9c; thw=cn; sgcookie=ETmpEUOWeot1QvhNHMYw5; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UNX%2FRabQf7RKzA%3D%3D&nk2=D8zlh3k8M9o5Pg%3D%3D&vt3=F8dBxd9koY4EyuRS5Zg%3D; lgc=louielouie; uc4=nk4=0%40De%2FPBpYsSfK9SgJzWf2E343jTyWA&id4=0%40UgJ6xtNFD8seIyRycNZIK1sxxV9L; tracknick=louielouie; _cc_=V32FPkk%2Fhw%3D%3D; tg=0; enc=FgUj65srs%2BHu2039WlqZz99vL7Mm138iexBU7ZHcxEyTuCm1c%2BUMQpp5fkVBImpL6H00Sn4In%2FiRo54Uah74sA%3D%3D; tfstk=c1bfB3AAMxDfisAj0GNy7LkTpDTOZ0wWZo9AGgOGJXkoid5fiO0edQlcjY0JvQ1..; mt=ci=-1_1; hng=CN%7Czh-CN%7CCNY%7C156; v=0; cookie2=5b37e99960f293f573ace663c80e5672; uc1=cookie14=UoTUPvgy4sbPow%3D%3D; _tb_token_=f7675165ebbde; JSESSIONID=FED28730AC1CD53DC72205AA96370D93; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; isg=BDQ0Z5331hAMO0LY7cnE_hbdBfKmDVj3zLPiC86Ve79TOdeD9h9Rh_37vXHhwZBP; l=dBPZQQJqQ1ZVZq1DBOfNNDE4CkbTwIRf1sPr9ZAIDICPOX16PX7RWZ4olTYBCnGVHsGBR3oGfmNDBb86lydqGhZfP3k_J_qq3dC..; _samesite_flag_=true'}

    try:
        r=requests.get(url,timeout=30,headers=kv,headers=ck)       # 获取
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text                               # 获取内容
    except:
        return ''                                   # 若有异常返回空值

def paserPage(ilt,html):
    try:
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        for i in range(len(tlt)):
            title=eval(tlt[i].split(':')[-1])  # eval函数可将获得的字符串最外层的引号去除；split函数选取分割符为冒号；[1]下标意为选最后一个部分
            price=eval(plt[i].split(':')[-1])
            ilt.append([title,price])          # 放入空列表ilt
    except:
        print('')


def printGoodsList(ilt):
    # 做第一行的表头    
    tplt='{0:^4}\t{1:^8}\t{2:^16}'
    print(tplt.format('序号','商品名称','价格'))
    
    # 做接下来的行
    count=0    # 做一个计数器，为序号准备
    for i in ilt:
        count+=1
        print(tplt.format(count,ilt[0],ilt[1]))



if __name__ == "__main__":
    goods='书包'
    depth=2
    start_url='https://s.taobao.com/search?q=' + goods
    inforList=[]
    for i in range(depth):
        try:
            url=start_url+ '&s=' + str(44*i)
            html=getHtmlText(url)
            paserPage(inforList,html)
        except:  # 若某一页面解析有问题，则跳过
            continue
    printGoodsList(inforList)
