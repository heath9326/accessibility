from sqlite3 import IntegrityError

from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from scraping.scraping.spiders import AItemSpider, FormItemSpider
from .models import Url
from scrapy.crawler import CrawlerProcess


class AutomaticAItemCrawler:
    """Automatic crawler to activate AType scrapy spider and store its items in the DB. """
    name = "AItem Crawler"
    url_id: int = None
    start_urls: list = []

    def __init__(self, url: str, url_id: int):
        self.url_id = url_id
        self.start_urls.append(url)

    def __str__(self):
        return "Automatic crawler for <<a>> page item"

    def crawl(self):
        #spider_kwargs = {} if spider_kwargs is None else spider_kwargs
        crawler = CrawlerProcess()
        crawler.start()
        crawler.crawl(AItemSpider, start_urls=self.start_urls, url_id=self.url_id)
        crawler.start(stop_after_crawl=True, install_signal_handlers=False)

    # def run_spider_main_spider(self):
    #     runner = CrawlerRunner(get_project_settings())
    #     runner.crawl(MainSpider, start_urls=self.start_urls, url_id=self.url_id)
    #     # TODO add other spiders here
    #     d = runner.join()
    #     d.addBoth(lambda _: reactor.stop())
    #     reactor.run(0)

    def scrape_page(self):
        self.crawl()

class AutomaticFormCrawler:
    """Automatic crawler to activate AType scrapy spider and store its items in the DB. """
    name = "Form Crawler"
    url_id: int = None
    start_urls: list = []

    def __init__(self, url: str, url_id: int):
        self.url_id = url_id
        self.start_urls.append(url)

    def __str__(self):
        return "Automatic crawler for <<form>> page item"

    def crawl(self):
        #spider_kwargs = {} if spider_kwargs is None else spider_kwargs
        crawler = CrawlerProcess()
        crawler.start()
        crawler.crawl(FormItemSpider, start_urls=self.start_urls, url_id=self.url_id)
        crawler.start(stop_after_crawl=True, install_signal_handlers=False)

    # def run_spider_main_spider(self):
    #     runner = CrawlerRunner(get_project_settings())
    #     runner.crawl(MainSpider, start_urls=self.start_urls, url_id=self.url_id)
    #     # TODO add other spiders here
    #     d = runner.join()
    #     d.addBoth(lambda _: reactor.stop())
    #     reactor.run(0)

    def scrape_page(self):
        self.crawl()

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

