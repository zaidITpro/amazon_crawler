# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name=scrapy.Field()
    product_sale_price=scrapy.Field()
    product_category=scrapy.Field()
    product_original_price=scrapy.Field()
    product_availability=scrapy.Field()
    pass
