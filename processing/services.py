from processing.models import AItem, Url
from processing.processors import ATypeProcessor, FormTypeProcessor, ImgTypeProcessor
from sqlite3 import IntegrityError

from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from scraping.scraping.spiders import AItemSpider, FormItemSpider
from .models import Url
from scrapy.crawler import CrawlerProcess

from .tasks import AutomaticCrawler


class AutomaticCrawlerService:
    automatic_crawler = AutomaticCrawler
    url_to_process: str = None
    url_id: str = None

    def __init__(self, url_to_process: str, url_id: int):
        print("Initializing AutomaticCrawlerService...")
        self.url_to_process = url_to_process
        self.url_id = url_id

    def __call__(self):
        print("AutomaticCrawlerService is being called...")
        try:
            automatic_crawler = AutomaticCrawler(self.url_to_process, self.url_id)
            automatic_crawler.crawl()
        except Exception as exc:
            self.clear_db()
            print(f"While scraping the page exeption occurred, exeption: {exc}")
            print(f"Fix the error and repeat the process")
            return

    def clear_db(self):
        url = Url.objects.get(url=self.url_to_process)
        url.delete()


class AccessibilityProcessingService:
    processors: set = (ATypeProcessor, FormTypeProcessor, ImgTypeProcessor)
    url_to_process: str = None
    url_id: int = None
    context: dict = {}

    def __init__(self, url_to_process: str,  url_id: int):
        print("Initializing AccessibilityProcessingService...")
        self.url_to_process = url_to_process
        self.url_id = url_id

    def __call__(self):
        print("AccessibilityProcessingService is called...")
        for processor in self.processors:
            try:
                active_processor = processor(self.url_id)
                elements = active_processor.process_elements()
                self.context[processor.name] = elements
            except Exception as exc:
                print(f"Exception occurred while processing and items, exception: '{exc}'")
        return self.context

    def clear_db(self):
        url = Url.objects.get(url=self.url_to_process)
        url.delete()

