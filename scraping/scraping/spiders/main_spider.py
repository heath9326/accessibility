import scrapy
from ..items import ATypeItem


#TODO links need to be sent from another django app
class MainSpider(scrapy.Spider):
    name = 'wholepage'
    start_urls = ['https://sfedu.ru/']

    # def __int__(self, start_urls: list[str]):
    #     self.start_urls = start_urls

    def parse(self, response):
        item = ATypeItem()
        custom_settings = {'ITEM_PIPELINES': {"scraping.pipelines.ScrapingPipeline": 300}}
        # Response.css('title').extract() to scrape only title
        a_elements = response.css('a').extract()
        for a_element in a_elements:
            #page_html = response.css('header::text').extract()
            item['a_element'] = a_element
            item['url'] = self.start_urls[0]
            yield item


# scrapy shell "https://sfedu.ru/" start scrapy shell
# response.css("title")
#page_html = response.css('header::text')[0].extract() fist element of the scraped list
#page_html = response.css('header::text').extract_first() - does not returb error if there are no element like this
#page_html = response.css('span.text).extract() - span element that has text class element inside it
#page_html = response.css('span.text::text).extract() - span element that has text class element inside it
#page_html = response.css('span#text).extract() - span element that has an elememn with id=text

#response.xpath("//a")
#response.xpath("//a/text()")
#response.xpath("//a[@class='text']")
#scpary crawl wholepage -o items.json