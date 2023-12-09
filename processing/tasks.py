from sqlite3 import IntegrityError

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraping.scraping.spiders import MainSpider
from .models import Url


class AutomaticCrawler:
    url_id: int = None
    start_urls: list = []

    def __init__(self, url: str, url_id: int):
        self.url_id = url_id
        self.start_urls.append(url)

    def run_spider_main_spider(self):
        process = CrawlerProcess(get_project_settings())
        process.crawl(MainSpider(self.start_urls))
        process.start()

    def scrape_page(self):
        self.run_spider_main_spider()
    #django_rq.enqueue(run_spider)


class UrlProcessor:
    url: str

    def __init__(self, url: str):
        self.url = url

    def process_url(self):
        try:
            new_url = Url.objects.create(url=self.url).save()
            new_url_id = new_url.id
            return new_url_id
        except Exception as exc:
            print(f"Exception occurred while saving instance, exception: {exc}")
            existing_url_id = Url.objects.get(url=self.url).id
            return existing_url_id

