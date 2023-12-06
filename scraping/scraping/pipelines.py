# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3

# TODO create the db first
class ScrapingPipeline:

    def __int__(self):
        pass

    def store_db(self, item):
        self.curr.execute("""insert into a_elements_tb values(?, ?)""", (item['a_element'], item['url']))
        self.conn.commit()

    def process_item(self, item, spider):
        self.conn = sqlite3.connect("scrapy_database.db")
        self.curr = self.conn.cursor()
        self.curr.execute("""CREATE TABLE IF NOT EXISTS a_elements_tb(element text, url text)""")
        self.store_db(item)
        return item

    def close_spider(self):
        self.curr.close()


