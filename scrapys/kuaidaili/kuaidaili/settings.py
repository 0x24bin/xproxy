# -*- coding: utf-8 -*-

# Scrapy settings for kuaidaili project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'kuaidaili'

SPIDER_MODULES = ['kuaidaili.spiders']
NEWSPIDER_MODULE = 'kuaidaili.spiders'

ITEM_PIPELINES = ['kuaidaili.pipelines.KuaidailiPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xroxy (+http://www.yourdomain.com)'

DOWNLOAD_DELAY = 0.5
