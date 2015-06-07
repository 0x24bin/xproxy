import scrapy
import re
from cnproxy.items import CnproxyItem

class thSpider(scrapy.spider.Spider):
	name = "cnproxy"
	allowed_domains = ["cn-proxy.com"]
	start_urls = [
		'http://cn-proxy.com/',
		'http://cn-proxy.com/archives/218'
	]

	def parse(self, response):

		reses = response.xpath(".//table/tbody/tr")

		for res in reses:
			item = CnproxyItem()
			item['tp'] = u'http'
			item['ip'] = res.xpath("td[1]/text()").extract()[0].strip()
			item['port'] = res.xpath("td[2]/text()").extract()[0].strip()

			yield item