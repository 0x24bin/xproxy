#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import requests
from pprint import pprint



def getTime(proxyurl,basicurl='http://www.baidu.com'):
	'''return mico seconds 
	@proxyurl
	@basicurl
	'''
	if proxyurl.startswith('http://'):
		proxies = {'http':proxyurl}
	elif proxyurl.startswith('https://'):
		proxies = {'https':proxyurl}

	repeattimes = 2
	timetotal = 0
	for x in xrange(1,repeattimes+1):
		timesec = 10
		start = time.time()
		try:
			rq = requests.get(basicurl,proxies=proxies,timeout=10)
			end = time.time()
			timesec = end - start
		except IOError,e:
			print IOError,e

		timetotal += int(timesec*1000)

	timeavrage = int(timetotal/repeattimes)
	return timeavrage

def check_proxies(proxies,basicurl='http://www.baidu.com',timeout=10000):
	'''
	@proxies:(type,ip,port)
	@basicurl:
	@timeout:
	'''
	proxies_avalible = []
	for each_proxy in proxies:
		proxy_type = proxies[0]
		proxy_url = '%s://%s:%s' % (each_proxy[0],each_proxy[1],each_proxy[2])
		timesec = getTime(proxy_url,basicurl)
		print proxy_url,'\ttimesec=',timesec
		if timesec<timeout:
			proxies_avalible.append(each_proxy)
	# pprint(proxies_avalible)
	return proxies_avalible


def read_proxies_from_file(filename):
	'''
	@filename:
	'''
	proxies = []
	with open(filename,'r') as fp:
		for line in fp:
			proxies.append(tuple(line.strip().split('\t')))

	return proxies

def write_proxies_2_file(filename,proxies):
	'''
	@filename:
	'''
	with open(filename,'r') as fp:
		for proxy in proxies:
			fp.write('\t'.join(proxy)+os.linesep)

def main():
	proxies = read_proxies_from_file('proxies2.txt')
	proxies_avalible = check_proxies(proxies,'http://lacnic.net/cgi-bin/lacnic/whois?lg=EN')
	write_proxies_2_file('proxies_avalible.txt', proxies_avalible)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()