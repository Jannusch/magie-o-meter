from magie_o_meter.db_config import inster_date_to_database
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from magie_o_meter.magie_o_meter.spiders.crawler import MagieSpider
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import os
from twisted.internet.task import deferLater
import time


def main():
    start_urls = []
    for i in range(1,13):
        for j in range(1,32):
            for k in range(2018,2020):
                if i < 10:
                    if j < 10:
                        date = f"0{j}-0{i}-{k}"
                        start_urls.append(f'https://tagesenergie.org/energie-des-tages/tagesenergie-am-{date}/')
                    else:
                        date = f"{j}-0{i}-{k}"
                        start_urls.append(f'https://tagesenergie.org/energie-des-tages/tagesenergie-am-{date}/')
                else:
                    if j < 10:
                        date = f"0{j}-{i}-{k}"
                        start_urls.append(f'https://tagesenergie.org/energie-des-tages/tagesenergie-am-{date}/')
                    else:
                        date = f"{j}-{i}-{k}"
                        start_urls.append(f'https://tagesenergie.org/energie-des-tages/tagesenergie-am-{date}/')



    for url in start_urls:
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        date = ''
        for i in range(59,67):
            date = date + url[i]
        time.sleep(5)
        process.crawl(MagieSpider, url=url, date=date)

def sleep(self, *args, seconds):
    """Non blocking sleep callback"""
    return deferLater(reactor, seconds, lambda: None)


process = CrawlerProcess(get_project_settings())


def _crawl(result, spider):
    deferred = process.crawl(spider)
    deferred.addCallback(lambda results: print('waiting 100 seconds before restart...'))
    deferred.addCallback(sleep, seconds=100)
    deferred.addCallback(_crawl, spider)
    return deferred

if __name__ == "__main__":
    main()