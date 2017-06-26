# -*- coding: utf-8 -*-
import scrapy


class BookItem(scrapy.Item):
    name = scrapy.Field()
    search_keywords = scrapy.Field()
    description = scrapy.Field()
    authors = scrapy.Field()
    publisher = scrapy.Field()
    translators = scrapy.Field()
    publish_at = scrapy.Field()
    page_count = scrapy.Field()
    price = scrapy.Field()
    isbn = scrapy.Field()
    catalogue = scrapy.Field()
    douban_tags = scrapy.Field()
    douban_score = scrapy.Field()
