# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3







conn.commit()
conn.close()


class ScrapingPipeline:

    def __int__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("scrapy_database.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS elements_tb""")
        self.curr.execute("""create table elements_tb(element text, utl text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into _tb values(?, ?, ?)""",(item['page_html']))
        self.conn.commit()
