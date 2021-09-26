from lxml import etree
import requests
import pandas
max_page=20
all_title=[]
all_time=[]
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
for page in range(1,max_page+1):
    print("爬取的页面是第{}页".format(page))
    url='http://guba.eastmoney.com/list,zssh000001_{}.html'.format(page)
    data=response=requests.get(url,headers)
    print(data.text)
    # data=etree.HTML(data.text)
    # # title=data.xpath('//div[contains(@class,"artcleh normal_post")]//span[@class="l3 a3"]//text()')
    # page_data = data.xpath('//a[@class="href"]/text()')
    # print(page_data)



