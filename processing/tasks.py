from scraping.scraping.spiders import AItemSpider, FormItemSpider, ImgItemSpider
from .models import Url
from scrapy.crawler import CrawlerProcess


class AutomaticCrawler:
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
        crawler = CrawlerProcess()
        crawler.start()
        crawler.crawl(FormItemSpider, start_urls=self.start_urls, url_id=self.url_id)
        crawler.crawl(AItemSpider, start_urls=self.start_urls, url_id=self.url_id)
        crawler.crawl(ImgItemSpider, start_urls=self.start_urls, url_id=self.url_id)
        crawler.start(stop_after_crawl=True, install_signal_handlers=False)


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

