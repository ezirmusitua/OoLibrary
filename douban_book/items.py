# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import TakeFirst

from .loader_processor import StripAndJoin, StripValues, DateStrToTimeStamp


class BookItem(scrapy.Item):
    default_output_processor = StripAndJoin()
    name = scrapy.Field(output_processor=TakeFirst())
    search_keywords = scrapy.Field(output_processor=StripValues())
    description = scrapy.Field()
    authors = scrapy.Field()
    publisher = scrapy.Field(output_processor=TakeFirst())
    translators = scrapy.Field(output_processor=StripValues())
    publish_at = scrapy.Field(output_processor=DateStrToTimeStamp())
    # TODO: From this
    page_count = scrapy.Field()
    price = scrapy.Field()
    isbn = scrapy.Field()
    catalogue = scrapy.Field()
    douban_tags = scrapy.Field()
    douban_score = scrapy.Field()
