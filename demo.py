#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author: yangbh

import time
import requests
from random import randint
from xproxy import XProxy

def main():
	xp = XProxy()
	xp.add_scrapy('scrapys/cnproxy', 'cnproxy')
	# xp.add_scrapy('scrapys/xroxy', 'xroxy')
	# 这里要用start，不要用run，以免进入jion()死循环
	xp.start()
	time.sleep(10)
	while True:
		print 'scrapy num:',len(xp.proxies)
		pr = xp.rand_proxy()
		print 'random get one proxy:', pr
		try:
			url = 'https://www.google.com.hk'
			proxies = {pr[0]:'%s://%s:%s' % tuple(pr)}
			rq = requests.post(url=url,proxies=proxies,timeout=5)
		except Exception,e:
			print 'Exception',e
			print 'remove proxy',pr
			xp.remove_proxy(pr)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()