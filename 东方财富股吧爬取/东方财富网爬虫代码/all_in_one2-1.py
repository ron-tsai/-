import requests


from lxml import etree
from fake_useragent import UserAgent

from time import sleep
import pandas as pd
import os

path='/Users/ccmac/Desktop/pc2'

def getHTMLText():
    tunnel = "tps371.kdlapi.com:15818"

    # 用户名密码方式
    username = "t14258150103392"
    password = "gc2h5zhq"
    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
    }


    df_list = os.listdir(path)
    num_list = list(range(70000, 85000))
    # print(num_list)
    complete_list = []
    for fname in df_list:
        complete_list.append(fname[:-5])
        # print(fname[:-5])
    for del_v in complete_list:
        # print(del_v)
        if del_v != '.DS_':
            del_v = int(del_v)
            num_list.remove(del_v)
    print(len(num_list))
    while True:

        headers = {
            'User-Agent': UserAgent().random  # #生成随机请求头
        }


        try:
            for num in num_list:
                url = 'http://guba.eastmoney.com/list,zssh000001,f_{}.html'.format(num)


                # 使用代理访问
                response = requests.get(url=url, headers=headers, proxies=proxies, timeout=15)


                if response.status_code == 200:
                    tree = etree.HTML(response.text)

                    title = tree.xpath(
                        '//*[@id="articlelistnew"]//span[@class="l3 a3"]/a/@title')
                    # title = title.encode('iso-8859-1','ignore').decode('GBK','ignore')

                    time = tree.xpath(
                        '//*[@id="articlelistnew"]//span[@class="l5 a5"]/text()'
                    )

                    time = time[1:]

                    df = pd.DataFrame({'time': time, 'title': title})
                    if df.empty == True:  ##empty不加（），判断df是否无数据
                        print('df为空')  ##报错退出

                    else:
                        df.to_excel(os.path.join(path, '{}.xlsx').format(num))
                else:
                    print('无效网页')
        except Exception:
            print("获取" + str(url) + "网页内容失败！")
            proxies = {
                "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
                "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
            }
            df_list = os.listdir(path)
            num_list = list(range(70000, 85000))
            # print(num_list)
            complete_list = []
            for fname in df_list:
                complete_list.append(fname[:-5])
                # print(fname[:-5])
            for del_v in complete_list:
                # print(del_v)
                if del_v != '.DS_':
                    del_v = int(del_v)
                    num_list.remove(del_v)
            print(len(num_list))
            # print(num_list)
        finally:
            sleep(0.2)

getHTMLText()