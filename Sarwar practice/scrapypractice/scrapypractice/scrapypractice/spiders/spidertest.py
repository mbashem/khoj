from time import sleep
from crochet import run_in_reactor, setup, wait_for
setup()

import time
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner

from twisted.internet import reactor



class testspider(scrapy.Spider):

    name = "testspider"
   
    DEPTH_PRIORITY = 1
    SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
    SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

    start_urls = [
            'https://quotes.toscrape.com/page/1/'
    ]
    


    def start_requests(self):
      
            return [scrapy.Request('https://quotes.toscrape.com/page/1/',callback=self.parse, cb_kwargs=dict(cnt = 1))]
        

         

    def parse(self,response,cnt):

        
        yield {'url' : response.url,'depth' : cnt}
        #print('THE CURRENT URL IS '+response.url)

        for txt in response.css("::text"):
            var = txt.get().strip()
            if len(var) != 0:
                yield {'text' : var}
         


        if(cnt<2):

             for nextpage in response.css('a::attr(href)'):
                 nextpage = nextpage.get()
                 if nextpage is not None:
                     #print('THE URL IS '+response.urljoin(nextpage))
                     yield scrapy.Request(response.urljoin(nextpage),callback=self.parse, cb_kwargs=dict(cnt = cnt+1))  
                     



@wait_for(timeout = 10.0)
def begin_crawl():
    
    process = CrawlerRunner(settings={"FEEDS": {"scrapped.json": {"format": "json"},},})
    d = process.crawl(testspider)
    print("crawl begun")
    return d
    
   
    
    
    
    
    


                    
begin_crawl()
print("its done")




