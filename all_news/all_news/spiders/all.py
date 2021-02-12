import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllSpider(CrawlSpider):
    name = 'all'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sou.chinanews.com/search.do?q=A%E8%82%A1']


    ###页码链接提取器：根据指定规则（allow='正则'）进行指定链接的提取
    link=LinkExtractor(allow=r'javascript:ongetkey(\d+)')
    link_detail=LinkExtractor(allow=r'')
    rules = (
        #规则解析器：将链接提取器提取到的链接进行指定规则的解析
        Rule(link, callback='parse_item', follow=True),
    )
    ###页面链接提取器

    #解析新闻标题和新闻页url
    def parse_item(self, response):
        hrefs=response.xpath('//li/a').extract()
        for href in hrefs:
            yield scrapy.Request('http:'+href,meta={'href':href},callback=self.parse)





