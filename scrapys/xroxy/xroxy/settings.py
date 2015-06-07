# -*- coding: utf-8 -*-

# Scrapy settings for xroxy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'xroxy'

SPIDER_MODULES = ['xroxy.spiders']
NEWSPIDER_MODULE = 'xroxy.spiders'

ITEM_PIPELINES = ['xroxy.pipelines.XroxyPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xroxy (+http://www.yourdomain.com)'

DOWNLOAD_DELAY = 0.5