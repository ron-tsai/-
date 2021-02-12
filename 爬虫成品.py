#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

from time import sleep
from lxml import etree
import pandas as pd

page_list=[]

if __name__=="__main__":
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"

    }

    url='http://sou.chinanews.com/search.do?q=A%E8%82%A1'
    df = pd.DataFrame(columns=['date_source', 'title', 'content','link'])

    for i in range(800,1001):
        print(i)
        page=10*i
        params={
            'q': 'A股',
            'ps':10,
            'start':page
        }
        sleep(2)
        response = requests.get(url=url,params=params,headers=headers)
        # response.encoding = 'UTF-8'  # 转码为UTF-8格式
        page_text=response.text

        tree=etree.HTML(page_text)
        page_link=tree.xpath('//li/a/@href')
        for link in page_link:
            try:
                print(link)
                sleep(2)
                response = requests.get(url=link, headers=headers)
                # response.encoding = 'UTF-8'  # 转码为UTF-8格式
                content_text=response.text
                tree=etree.HTML(content_text)

                title = tree.xpath('//h1[@style="display:block; position:relative; clear:both"]/text()|//h1[@style="display:block; position:relative; text-align:center; clear:both"]/text()')[0]
                title = title.encode('iso-8859-1','ignore').decode('GBK','ignore')

                # print(title)


                date_source = tree.xpath('//div[@class="left-t"]/text()')[0]
                date_source = date_source.encode('iso-8859-1','ignore').decode('GBK','ignore')
                contents = tree.xpath('//div[@class="left_zw"]/p')
                # print(title)



            except:
                continue




            contain = ''
            for content in contents:
                try:content=content.xpath('./text()')[0]
                except:
                    continue
                content=content.encode('iso-8859-1','ignore').decode('gbk','ignore')
                # print(content)

                contain = contain + ' ' + content
            s = pd.Series([date_source, title, contain,link], index=['date_source', 'title', 'content','link'])
            df = df.append(s, ignore_index=True)

    df.to_excel('C:\\Users\Administrator\Desktop\\八百到一千.xlsx')




