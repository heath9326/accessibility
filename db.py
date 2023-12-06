import sqlite3

conn = sqlite3.connect("scrapy_database.db")
curr = conn.cursor()
curr.execute("""CREATE TABLE IF NOT EXISTS a_elements_tb(element text, url text)""")
conn.commit()
conn.close()
