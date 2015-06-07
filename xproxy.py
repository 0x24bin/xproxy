#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author: yangbh

import os
import threading, time, random

from random import randint
from proxy_check import *

class XProxy(threading.Thread):
	"""docstring for XProxy"""
	def __init__(self, minnum=100, maxnum=1000, scrapys=None):
		super(XProxy, self).__init__()
		self.min = minnum
		self.max = maxnum
		self.proxies = list()
		self.scrapys = list()

	def add_scrapy(self, scrapypath, scrapyname):
		''' 增加一个scrapy抓取接口
		'''
		self.scrapys.append((scrapypath,scrapyname))

	def run(self):
		''' 开始运行，确保proxies的数量在min到max区间内
		'''
		while True:
			if len(self.proxies) < self.min:
				print '[*][-] proxies tow few, scrapy some'
				for scrapy in self.scrapys:
					self._run_scrapy(scrapy)
					if len(self.proxies) > self.max:
						print '[*][-] proxies tow many, stop scrapy'
						break
			time.sleep(10)

	def remove_proxy(self, proxy):
		''' 删除一个接口
		'''
		self.proxies.remove(proxy)

	def rand_proxy(self,proxiestype='http'):
		''' 随机返回http/https代理
		'''
		# print '[*][-] in pid:',os.getpid(),'total proxies num:',len(g_proxies)
		num = len(self.proxies) - 1
		if num > 0:
			i = randint(0, num)
			return self.proxies[i]
	
	def _run_scrapy(self,scrapy):
		''' 利用scrapy抓取代理接口
		@scrapypath: scrapy project path
		@spidername: scrapy spider name
		'''
		try:
			scrapypath = scrapy[0]
			spidername = scrapy[1]
			pwd = os.getcwd()
			os.chdir(scrapypath)
			# print os.getcwd()
			os.popen('scrapy crawl %s' % spidername)
			os.chdir(pwd)
			# os.rename(scrapypath+'/proxies.txt', pwd+'/proxies_new.txt')
			
			proxies = read_proxies_from_file(scrapypath+'/proxies.txt')
			print 'len:',len(proxies)
			for i in proxies:
				if i not in self.proxies:
					self.proxies.append(i)

		except Exception,e:
			print 'Exception',e
			# traceback.print_exc(file=sys.stdout)

	def flush(slef):
		''' 删除所有proxies
		'''
		self.proxies = list()
