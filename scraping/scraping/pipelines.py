# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3


class ScrapingPipeline:
    conn = None
    curr = None

    def __int__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("scrapy_database.db")
        self.curr = self.conn.cursor()
        return self.conn, self.curr

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS a_elements_tb(element text, url text)""")

    def store_db(self, item):
        self.curr.execute("""insert into a_elements_tb values(?, ?)""", (item['a_element'], item['url']))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item


