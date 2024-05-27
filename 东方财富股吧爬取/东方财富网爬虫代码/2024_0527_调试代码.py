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
    # while True:
        headers = {
            'User-Agent':UserAgent().random
        }
        try:
            url = 'http://guba.eastmoney.com/list,zssh000001,f_{}.html'.format(1)
            # 使用代理访问
            response = requests.get(url=url, headers=headers, timeout=15)

            # 将HTML文档字符串解析为Element对象

            if response.status_code == 200:
                tree = etree.HTML(response.content)

                script = tree.xpath(
                    '/html/body/script[1]/text()'
                )

                data=script[0]
                print(data)
                obj=re.compile(r'var article_list=(?P<json>.*?);')

                content=obj.search(data).group('json')
                print(content)
                dic=json.loads(content)  #好像是变成python字典对象
                lst=dic["re"]
                print(lst)
                for each in lst:
                    title=each["post_title"]
                    user=each["user_nickname"]
                    time=each["post_publish_time"]
                    print(title,user,time)


            else:
                print('无效网页')
        except Exception:
            print("获取网页内容失败！")


getHTMLText()