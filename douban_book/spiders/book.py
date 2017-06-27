# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider

from douban_book.items import BookItem


class BookSpider(CrawlSpider):
    name = 'book_detail'
    allowed_domains = ['douban.com']
    search_url_base = 'https://book.douban.com/subject_search?search_text={}'

    def start_requests(self):
        url = ''
        keyword_str = getattr(self, 'keywords', '')
        if keyword_str is not '':
            url = BookSpider.search_url_base.format(keyword_str)
        yield scrapy.Request(url, self.parse_search)

    def parse_search(self, response):
        register_link = response.xpath('//*[@id="content"]/div/div[1]/p/span/a/@href').extract_first()
        if register_link is not None and 'register' in register_link:
            yield None
            return
        book_link = response.xpath('//*[@id="content"]/div/div[1]/ul/li[1]/div[2]/h2/a/@href').extract_first()
        if book_link is None:
            yield None
            return
        yield scrapy.Request(book_link, self.parse_book)

    def parse_book(self, response):
        book_loader = ItemLoader(item=BookItem(), response=response)
        book_loader.add_xpath('name', '//*[@id="wrapper"]/h1/span/text()')
        book_loader.add_value('search_keywords', getattr(self, 'keywords', '').split(','))
        book_loader.add_xpath('description', '//*[@id="link-report"]/div[1]/div/p/text()')
        book_loader.add_xpath('authors', '//*[@id="info"]/span[1]/a/text()')
        book_loader.add_xpath('publisher', '//*[@id="info"]/text()[1]')
        book_loader.add_xpath('translators', '//*[@id="info"]/span[3]/a/text()')
        book_loader.add_xpath('publish_at', '//*[@id="info"]/text()[2]')
        book_loader.add_xpath('page_count', '//*[@id="info"]/text()[3]')
        book_loader.add_xpath('isbn', '//*[@id="info"]/text()[7]')
        book_loader.add_xpath('catalogue', '//*[@id="dir_1921890_full"]/text()')
        book_loader.add_xpath('douban_tags', '//*[@id="db-tags-section"]/div/span/a/text()')
        book_loader.add_xpath('douban_score', '//*[@id="interest_sectl"]/div/div[2]/strong/text()')
        return book_loader.load_item()
