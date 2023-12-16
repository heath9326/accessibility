import scrapy
from ..items import ATypeItem
from processing.models import AItem, FormItem, ImgItem


class ImgItemSpider(scrapy.Spider):
    name = 'imgitem'
    start_urls = []
    url_id = None

    def __int__(self, *args, **kwargs):
        self.start_urls = kwargs.get('start_urls', [])
        self.url_id = kwargs.get('url_id', [])
        super(ImgItemSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # item = ATypeItem()
        # custom_settings = {'ITEM_PIPELINES': {"scraping.pipelines.AItemPipeline": 300}}
        # Response.css('title').extract() to scrape only title
        img_elements = response.xpath('//img').extract()
        for form_element in img_elements:
            #page_html = response.css('header::text').extract()
            item = ImgItem(element=form_element, url_id=self.url_id)
            #item['a_element'] = a_element
            #item['url_id'] = self.url_id
            yield item.save()