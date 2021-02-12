# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinanewsItem(scrapy.Item):
    source_name=scrapy.Field()
    source_url=scrapy.Field()
    title=scrapy.Field()
    author=scrapy.Field()
    publish_time=scrapy.Field()
