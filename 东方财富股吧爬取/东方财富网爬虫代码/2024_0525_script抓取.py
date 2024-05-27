import requests


from lxml import etree
from fake_useragent import UserAgent
import json

from time import sleep
import pandas as pd
import os
import re

path='/Users/ccmac/Desktop/pachong'


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
    num_list = list(range(1, 85000))
    # print(num_list)
    complete_list = []
    for fname in df_list:

        complete_list.append(fname[:-5])  ##文件名倒退5个字符，留下数字（去除.xlsx）
        # print(fname[:-5])
    for del_v in complete_list:
        # print(del_v)
        if del_v != '.DS_':
            del_v = int(del_v)
            num_list.remove(del_v)



    add_num = [num - 3 for num in num_list[:3]]  #在未爬取的页面中，往前增加3个页面，再爬一次这3个页面
    num_list = num_list + add_num
    num_list = sorted(num_list)


    while True:

        headers = {
            'User-Agent':UserAgent().random
        }

        try:
            for num in num_list:

                url = 'http://guba.eastmoney.com/list,zssh000001,f_{}.html'.format(num)


                # 使用代理访问
                response = requests.get(url=url, headers=headers, proxies=proxies, timeout=15)

                # 将HTML文档字符串解析为Element对象


                if response.status_code == 200:

                    data=response.text
                    tree = etree.HTML(response.text)

                    script = tree.xpath(
                        '/html/body/script[1]/text()'
                    )
                    obj=re.compile(r"var article_list=\((?P<json>.*?)\);")

                    content=obj.search(data).group('json')
                    dic=json.loads(content)
                    print(dic)
                    # diff=dic["data"]["diff"]






                    # reply=tree.xpath(
                    #     '//tbody/tr//div[contains(@class,"reply")]/text()'
                    # )
                    # read=tree.xpath(
                    #     '//tbody/tr//div[contains(@class,"read" )]/text()'
                    # )
                    # title = tree.xpath(
                    #     '//tbody/tr//div[@class="title"]//a//text()')
                    # # title = title.encode('iso-8859-1','ignore').decode('GBK','ignore')
                    #
                    # time = tree.xpath(
                    #     '//tbody/tr//div[contains(@class,"update" )]/text()')
                    #
                    # author= tree.xpath(
                    #     '//tbody/tr//div[contains(@class,"author") ]//text()'
                    # )

                    # print(title)
                    # print(len(title))
                    # print(time)
                    # print(len(time))
                    # print(author)
                    # print(len(author))
                    # print(reply)
                    # print(len(reply))
                    # print(read)
                    # print(len(read))


                    sleep(1)

                    df = pd.DataFrame({'time': time, 'title': title, 'author': author, 'reply': reply,'read': read})
                    print(df)
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
            num_list = list(range(1, 85000))
            # print(num_list)
            complete_list = []
            for fname in df_list:
                complete_list.append(fname[:-5]) ##文件名倒退5个字符，留下数字（去除.xlsx）
                # print(fname[:-5])
            for del_v in complete_list:
                # print(del_v)
                if del_v != '.DS_':
                    del_v = int(del_v)
                    num_list.remove(del_v)
            print(len(num_list))
            add_num = [num - 3 for num in num_list[:3]]  # 在未爬取的页面中，往前增加3个页面，再爬一次这3个页面
            num_list = num_list + add_num
            # print(num_list)
        finally:
            sleep(0.2)

getHTMLText()