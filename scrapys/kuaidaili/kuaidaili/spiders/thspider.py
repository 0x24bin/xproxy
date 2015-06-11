import scrapy
import re
from kuaidaili.items import KuaidailiItem

class thSpider(scrapy.spider.Spider):
	name = "kuaidaili"
	allowed_domains = ["kuaidaili.com"]
	start_urls = list()
	for i in xrange(1,11):
		start_urls.append('http://www.kuaidaili.com/proxylist/%d/' % i)
	# start_urls = [
	# 	'http://www.kuaidaili.com/proxylist/1/',
	# ]

	def parse(self, response):

		reses = response.xpath(".//table/tbody/tr")

		for res in reses:
			item = KuaidailiItem()
			item['ip'] = res.xpath("td[1]/text()").extract()[0].strip()
			item['port'] = res.xpath("td[2]/text()").extract()[0].strip()
			tp = res.xpath("td[4]/text()").extract()[0].strip()
			if 'https' in tp.lower():
				item['tp'] = u'https'
			else:
				item['tp'] = u'http'
			yield item

		# num = response.xpath(".//div[@id='listnav']/ul/li/a[@class='active']/text()").extract()[0]
		# Npage = int(num)
		# num = response.xpath(".//div[@id='listnav']/ul/li/a[@class='active']/text()").extract()[0]
		# Apage = int(num)/10
		