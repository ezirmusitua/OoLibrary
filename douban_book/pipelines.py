# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.exporters import JsonItemExporter


class JsonExporterPipeline(object):
    def __init__(self):
        self.file = None
        self.exporter = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)

    def spider_opened(self, spider):
        self.file = open('spider-%s.json' % spider.name, 'w+b')
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()
        pass

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        pass

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
