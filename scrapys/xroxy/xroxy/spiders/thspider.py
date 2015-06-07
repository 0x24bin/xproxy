import scrapy
import re
from xroxy.items import XroxyItem

class thSpider(scrapy.spider.Spider):
	name = "xroxy"
	allowed_domains = ["xroxy.com"]
	baseurl = "http://www.xroxy.com/proxylist.php?port=&type=All_http&ssl=&country=&latency=&reliability=7500&sort=reliability&desc=true&pnum=0"
	Npage = 0
	Apage = 5
	start_urls = [
		baseurl+str(Npage)
	]

	def parse(self, response):

		reses = response.xpath(".//*[@id='content']/table[1]/tr[@class='row1' or @class='row0']")

		for res in reses:
			item = XroxyItem()
			item['ip'] = res.xpath("td[2]/a/text()").extract()[0].strip()
			item['port'] = res.xpath("td[3]/a/text()").extract()[0].strip()
			item['tp'] = 'http'
			yield item

		num = response.xpath(".//*[@id='content']/table[2]/tr/td[1]/table/tr[1]/td/small/a/b/text()").extract()[0]
		self.Npage = int(num.replace('Page ','').strip())
		num = response.xpath(".//*[@id='content']/table[2]/tr/td[1]/table/tr[2]/td/small/b/text()").extract()[0]
		self.Apage = int(num)/10
		print "************%d/%d**************" % (self.Npage,self.Apage)
		if self.Npage < self.Apage-1:
			yield scrapy.Request(self.baseurl+str(self.Npage+1), callback=self.parse)
		else:
			print "[+] Seems like to finish:)"
			exit()