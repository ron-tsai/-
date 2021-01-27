import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.cnstock.com/news/sns_jg/index.html#']


    def parse(self, response):
        li_list=response.xpath('//ul[@id="j_waterfall_list"]/li')
        print(li_list)
        for li in li_list:
            biaoti=li.xpath('./h2[1]/a/text()').extract_first()
            # biaoti=''.join(biaoti)
            print(biaoti)
