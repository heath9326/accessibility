# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3

class AItemPipeline:

    def __int__(self):
        pass

    def store_db(self, item):
        self.curr.execute("""insert into a_elements_tb values(?, ?)""", (item['a_element'], item['url_id']))
        self.conn.commit()

    def process_item(self, item, spider):
        print("PROCESSING ITEM")
        path = ("../scraping.sqlite3")
        self.conn = sqlite3.connect(path)
        self.curr = self.conn.cursor()
        self.curr.execute("""CREATE TABLE IF NOT EXISTS a_elements_tb(element text, url_id)""")
        self.store_db(item)
        return item

    def close_spider(self, spider):
        self.curr.close()


