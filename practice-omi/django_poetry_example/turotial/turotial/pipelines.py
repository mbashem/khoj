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


    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()



    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_table values(?,?,?)""",(
            item['title'][0],
            item['author'][0],
            item['tags'][0]
        ))

        self.conn.commit()