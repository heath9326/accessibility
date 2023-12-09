from processing.processors import ATypeProcessor
from processing.tasks import AutomaticCrawler


class AutomaticCrawlerService:
    crawlers: set = (AutomaticCrawler, )
    url_to_process: str = None
    url_id: str = None

    def __init__(self, url_to_process: str, url_id: int):
        print("Initializing AutomaticCrawlerService...")
        self.url_to_process = url_to_process
        self.url_id = url_id

    def __call__(self):
        print("AutomaticCrawlerService is being called...")
        for crawler in self.crawlers:
            try:
                active_crawler = crawler(self.url_to_process, self.url_id)
                active_crawler.scrape_page()
            except Exception as exc:
                print(f"While scraping the page using {crawler} exeption occurred, exeption: {exc}")
                print(f"Fix the error and repeat the process")
                # TODO collapse collected data
                return


class AccessibilityProcessingService:
    processors: set = (ATypeProcessor, )
    url_to_process: str = None
    url_id: int = None

    def __init__(self, url_to_process: str,  url_id: int):
        print("Initializing AccessibilityProcessingService...")
        self.url_to_process = url_to_process
        self.url_id = url_id

    def __call__(self):
        print("AccessibilityProcessingService is called...")
        for processor in self.processors:
            try:
                active_processor = processor(self.url_id)
                active_processor.process_elements()
            except Exception as exc:
                print(f"Exception occurred while processing and items, exception: '{exc}'")


