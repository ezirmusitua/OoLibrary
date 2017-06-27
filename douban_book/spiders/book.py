# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider

from douban_book.items import BookItem


def lint_info_content(content):
    striped_content = content.strip()
    if striped_content.startswith('\n') or striped_content is '':
        return None
    return content.strip()

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
        name = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()
        book_loader.add_value('search_keywords', getattr(self, 'keywords', '').split(','))
        book_loader.add_xpath('description', '//*[@id="link-report"]/div[1]/div/p/text()')
        book_loader.add_xpath('douban_tags', '//*[@id="db-tags-section"]/div/span/a/text()')
        book_loader.add_xpath('douban_score', '//*[@id="interest_sectl"]/div/div[2]/strong/text()')
        book_loader.add_xpath('catalogue', '//*[@id="dir_1921890_full"]/text()')
        book_loader.add_xpath('authors', '//*[@id="info"]/span[1]/a/text()')
        info_labels = list(map(lambda x: x.strip(),
                               response.xpath('//*[@id="info"]//span[contains(concat(" ", @class, " "), "pl")]/text()')
                               .extract()))
        info_contents = list(filter(lambda x: x is not None,
                                    map(lint_info_content, response.xpath('//*[@id="info"]/text()').extract())))
        translators_index = next((i for i, x in enumerate(info_labels) if x == '译者:'), -1)
        if translators_index > 0:
            book_loader.add_xpath('translators', '//*[@id="info"]/span[{}]//a/text()'.format(translators_index + 1))
        info_labels = list(filter(lambda x: x != '作者' and x != '译者' and x != '丛书:', info_labels))
        self.logger.info(info_labels)
        self.logger.info(info_contents)
        for index, label in enumerate(info_labels):
            self.logger.info(label)
            if label == '作者' or label == '译者':
                continue
            if label == '出版社:':
                book_loader.add_value('publisher', info_contents[index])
            if label == '副标题:':
                name += info_contents[index]
            if label == '出版年:':
                book_loader.add_value('publish_at', info_contents[index])
            if label == '页数:':
                book_loader.add_value('page_count', info_contents[index])
            if label == 'ISBN:':
                book_loader.add_value('isbn', info_contents[index])
        return book_loader.load_item()
