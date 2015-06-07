# -*- coding: utf-8 -*-

# Scrapy settings for cnproxy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cnproxy'

SPIDER_MODULES = ['cnproxy.spiders']
NEWSPIDER_MODULE = 'cnproxy.spiders'

ITEM_PIPELINES = ['cnproxy.pipelines.CnproxyPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xroxy (+http://www.yourdomain.com)'

DOWNLOAD_DELAY = 0.5