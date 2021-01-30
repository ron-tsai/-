import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.cnstock.com/news/sns_jg/index.html']


    def parse(self, response):
        li_list=response.xpath('//ul[@id="j_waterfall_list"]/li')
        # print(li_list)
        for li in li_list:
            link=li.xpath('./h2/a/@href').extract_first()
            title=li.xpath('./h2/a/text()').extract_first()
            date=li.xpath('./p[2]/span').extract_first()
            print(link,title,date)
