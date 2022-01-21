import requests


from lxml import etree
from fake_useragent import UserAgent


import pandas as pd
import os

path='/Users/ccmac/Desktop/pachong'



headers = {
    'User-Agent': UserAgent().random  # #生成随机请求头
}



url = 'http://guba.eastmoney.com/list,zssh000001,f_2004.html'


# 使用代理访问
response = requests.get(url=url, headers=headers,timeout=15)


if response.status_code == 200:
    tree = etree.HTML(response.text)

    title = tree.xpath(
        '//*[@id="articlelistnew"]//span[@class="l3 a3"]/a/@title')

    # title = title.encode('iso-8859-1','ignore').decode('GBK','ignore')
    print(title)

    time = tree.xpath(
        '//*[@id="articlelistnew"]//span[@class="l5 a5"]/text()'
    )

    time = time[1:]

    df = pd.DataFrame({'time': time, 'title': title})



    df.to_excel(os.path.join(path, '1111.xlsx'))






