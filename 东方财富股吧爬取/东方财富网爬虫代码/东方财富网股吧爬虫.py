from lxml import etree
import requests
import pandas as pd
from time import sleep
import random
import os

from fake_useragent import UserAgent

import traceback

url = "https://api.haohanfuwu.com/api/v1/ip"

body = {
    "login_name": "2641142613",
    "login_pwd": "PXKXaxxxFSFSAYCa"
}








path='/Users/ccmac/Desktop/爬虫文件存储'




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



# try:
#     res = requests.post(url, data=body, verify=False, timeout=3)
#     print(res.json())
#     result = res.json()
#     code = result['code']
#     if code == -1:
#         raise Exception("授权失败，请检查账号密码是否正确")
#     elif code == -2:
#         raise Exception("账号异常")
#     elif code == -3:
#         raise Exception("请求频率过快")
#     elif code == -4:
#         raise Exception("服务器错误")
#
#     proxy = result['data']
#
# except:
#     print(traceback.format_exc())


# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
headers = {
    'User-Agent': UserAgent().random  # #生成随机请求头
}
for num in num_list:
    a = random.random()
    sleep(a)
    print("爬取的页面是第{}页".format(num))
    url1 = 'http://guba.eastmoney.com/list,zssh000001_{}.html'.format(num)
    response = requests.get(url=url1, headers=headers, timeout=15)
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




