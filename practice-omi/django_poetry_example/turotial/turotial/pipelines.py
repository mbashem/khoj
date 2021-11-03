# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import  sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#Scraped data ---> Item Containers ---> Json/csv files
#Scraped data ---> Item Containers ---> pipeline ---> Database


class TurotialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()


    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_store""")
        self.curr.execute("""create table quotes_store(
            texts text,
            len int
            
            )""")



    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_store values(?,?)""",(
            item['texts'],
            item['len']
        ))

        self.conn.commit()