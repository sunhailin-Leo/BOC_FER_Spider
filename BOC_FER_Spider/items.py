# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BocFerSpiderItem(scrapy.Item):
    exchange = {}

    def __setitem__(self, key, value):
        self.exchange[key] = value
