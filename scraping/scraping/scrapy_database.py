import sqlite3

conn = sqlite3.connect("scrapy_database.db")
curr = conn.cursor()

curr.execute("""create table elements_tb(element text, utl text)""")

curr.execute("""insert into _tb values""")
conn.commit()
conn.close()