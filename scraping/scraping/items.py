# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ATypeItem(scrapy.Item):
    a_element = scrapy.Field()
    url_id = scrapy.Field()
