from all_in_one import getHTMLText
from ipGeter import ipGet
import os
import pandas as pd
path='/Users/ccmac/Desktop/pachong'

proxies=ipGet()
print(proxies)

num_list=list(range(2000,70000))

for num in num_list:

    url1 = 'http://guba.eastmoney.com/list,zssh000001,f_{}.html'.format(num)

    headers = {
        'User-Agent': UserAgent().random  # #生成随机请求头
    }


    response = requests.get(url=url1, headers=headers, proxies=proxies,timeout=15).text

    tree = etree.HTML(response)

    title = tree.xpath(
        '//*[@id="articlelistnew"]//span[@class="l3 a3"]/a//text()')
    # title = title.encode('iso-8859-1','ignore').decode('GBK','ignore')

    time = tree.xpath(
        '//*[@id="articlelistnew"]//span[@class="l5 a5"]/text()'
    )

    time = time[1:]

    df = pd.DataFrame({'time': time, 'title': title})
    if df.empty == True:  ##empty不加（），判断df是否无数据
        exit(1)  ##报错退出

    else:
        df.to_excel(os.path.join(path, '{}.xlsx').format(num))

proxies = ipGet()
print(proxies)