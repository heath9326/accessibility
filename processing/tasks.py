import django_rq

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraping.scraping.spiders import MainSpider


class AutomaticCrawler:
    start_urls = []

    def __int__(self, url: str):
        self.start_urls.append(url)

    def run_spider_main_spider(self):
        process = CrawlerProcess(get_project_settings())
        process.crawl(MainSpider(self.start_urls))
        process.start()

    def scrape_page(self):
        self.run_spider_main_spider()
    #django_rq.enqueue(run_spider)