#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

from time import sleep
from lxml import etree
if __name__=="__main__":

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"

    }
    link='http://www.chinanews.com/stock/2017/06-21/8256520.shtml'

    sleep(2)
    response = requests.get(url=link, headers=headers)
    # response.encoding = 'UTF-8'  # 转码为UTF-8格式
    content_text = response.text
    tree = etree.HTML(content_text)
    try:
        title = tree.xpath('//*[@id="cont_1_1_2"]/h1/text()')[0]
        title=title.encode('iso-8859-1').decode('GBK')

        date_source = tree.xpath('//*[@id="cont_1_1_2"]/div[3]/div/text()')[0]
        date_source=date_source.encode('iso-8859-1').decode('GBK')
        contents = tree.xpath('//*[@id="cont_1_1_2"]/div[5]/p')
    except:
        pass

    print(title)
