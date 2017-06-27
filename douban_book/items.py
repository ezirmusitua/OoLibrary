# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import TakeFirst

from .loader_processor import StripAndJoin, StripValues, DateStrToTimeStamp, FirstInteger, FirstFloat


class BookItem(scrapy.Item):
    default_output_processor = StripAndJoin()
    book_id = scrapy.Field()
    douban_book_id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    search_keywords = scrapy.Field(output_processor=StripValues())
    description = scrapy.Field()
    authors = scrapy.Field()
    publisher = scrapy.Field(output_processor=TakeFirst())
    translators = scrapy.Field(output_processor=StripValues())
    publish_at = scrapy.Field(output_processor=DateStrToTimeStamp())
    page_count = scrapy.Field(output_processor=FirstInteger())
    isbn = scrapy.Field()
    catalogue = scrapy.Field()
    douban_tags = scrapy.Field(output_processor=StripValues())
    douban_score = scrapy.Field(output_processor=FirstFloat())