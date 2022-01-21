
# -*- coding: utf-8 -*-
from lxml import etree

import pandas as pd
from time import sleep
import random
import os

from fake_useragent import UserAgent
import requests
import traceback












path='/Users/ccmac/Desktop/pachong'




df_list=os.listdir(path)
num_list=list(range(2000,70000))
# print(num_list)
complete_list=[]
for fname in df_list:
    complete_list.append(fname[:-5])
    # print(fname[:-5])
for del_v in complete_list:
    # print(del_v)
    if del_v!='.DS_':

        del_v=int(del_v)
        num_list.remove(del_v)
print(len(num_list))
# print(num_list)






headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
# 动态IP爬虫.py
for num in num_list:
    a = random.random()
    # sleep(a)
    print("爬取的页面是第{}页".format(num))
    api_url='http://api.sgxz.cn:12080/getip?token=cfd32d1b08717771953d98620f09332b&protocol=HTTP&num=200&result_format=JSON&separator=%5Cn&ip_dedup=0&time_avail=1'

    # proxies = {'协议': '协议://IP:端口号'}


    res = requests.post(api_url, headers=headers, verify=True)
    proxie = "https://%s" % (res.text)
    proxies = {'http': proxie}
    print(proxies)

    url1 = 'http://guba.eastmoney.com/list,zssh000001,f_{}.html'.format(num)
    response = requests.get(url=url1, headers=headers, proxies=proxies,timeout=15)
    content_text = response.text
    tree = etree.HTML(content_text)

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




