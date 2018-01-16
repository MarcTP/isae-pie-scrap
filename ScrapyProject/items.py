# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyItem(scrapy.Item):
	
	source = scrapy.Field()
	date = scrapy.Field()
	title = scrapy.Field()
	brief = scrapy.Field()
	url = scrapy.Field()
