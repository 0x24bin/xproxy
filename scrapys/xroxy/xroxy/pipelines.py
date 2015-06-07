# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XroxyPipeline(object):
    def __init__(self):
        self.fp = open("proxies.txt","w")

    def process_item(self, item, spider):
		self.fp.write("%s\t%s\t%s" % (item['tp'],item['ip'],item['port']))
		self.fp.write("\n")
		return item
