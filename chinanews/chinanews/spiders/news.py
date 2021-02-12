
import scrapy
import re
from chinanews.items import ChinanewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sou.chinanews.com/search.do?q=A%E8%82%A1']

    def parse(self, response):
        hrefs=response.xpath('//li/a/@href').extract()
        for href in hrefs:
            # print(hrefs)
            yield scrapy.Request('http:' + href, meta={'href': href}, callback=self.parsel)


        def parsel(self,response):
            item=ChinanewsItem()
            item['source_url']=self.start_urls
            item['source_url']='http:'+response.meta('href')
            print(item['source_url'])