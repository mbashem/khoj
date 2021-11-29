import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


import scrapy
import indexer.insert
from scrapy.crawler import CrawlerProcess

class nonhtml_spider(scrapy.Spider):

    name = "nonhtml_spider"
   
    #DEPTH_PRIORITY = 1
    #SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
    #SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

    start_urls = [
            'https://quotes.toscrape.com/page/1/'
    ]
    
    
    def start_requests(self):
        self.urllist = []
        for link in self.urls:
            self.urllist.append(scrapy.Request(link,callback=self.parse, cb_kwargs=dict(cnt = 1,root_url = link)))
        return self.urllist
            
    def parse(self,response,cnt,root_url):

        
        yield {'url' : response.url,'depth' : cnt}
        

        for txt in response.css("::text"):
            var = txt.get().strip()
            if len(var) != 0:
                print(var)
                print(cnt)
                print(root_url)
                print(response.url)

                indexer.insert.insert_into_solr_text( var, cnt, root_url, response.url, "nonhtml")
                yield {'text' : var}
         


        if(cnt<self.depth):

             for nextpage in response.css('a::attr(href)'):
                 nextpage = nextpage.get()
                 if nextpage is not None:
                     #print('THE URL IS '+response.urljoin(nextpage))
                     yield scrapy.Request(response.urljoin(nextpage),callback=self.parse, cb_kwargs=dict(cnt = cnt+1,root_url = root_url))  
                     

def begin_crawl(URLS,height):
    process = CrawlerProcess(settings={
    "FEEDS": {
        "scrapped.json": {"format": "json"},
    },
    "DEPTH_PRIORITY" : 1,
    "SCHEDULER_DISK_QUEUE" : 'scrapy.squeues.PickleFifoDiskQueue',
    'SCHEDULER_MEMORY_QUEUE' : 'scrapy.squeues.FifoMemoryQueue',

    })
    process.crawl(nonhtml_spider,urls = URLS,depth = height)
    process.start()



#begin_crawl(URLS = ['https://quotes.toscrape.com/page/1/'],height = 1)



#indexer.insert.insert_into_solr_text( 'New text', 5, 'root_url2','resposnse url 2',  "nonhtml")
#print("run succesfully")

                    
