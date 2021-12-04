import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from crochet import setup,run_in_reactor

import scrapy
import indexer.insert
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner


#This is the crawler class for collecting nonhtml data
class nonhtml_spider(scrapy.Spider):

    name = "nonhtml_spider"
   
    #DEPTH_PRIORITY = 1
    #SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
    #SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

    #This can be ignored
    start_urls = [
            'https://quotes.toscrape.com/page/1/'
    ]
    
    #This is the function that starts the crawling process
    def start_requests(self):
        self.urllist = []
        for link in self.urls:
            self.urllist.append(scrapy.Request(link,callback=self.parse, cb_kwargs=dict(cnt = 1,root_url = link)))
        return self.urllist
    #This is the callback function used to process the response
    def parse(self,response,cnt,root_url):
        
        yield {'url' : response.url,'depth' : cnt}

        for txt in response.css("::text"):

            var = txt.get().strip()

            if len(var) != 0:
                #If the text is not empty we insert it into solr
                indexer.insert.insert_into_solr_text( var, cnt, root_url, response.url, "nonhtml")
                yield {'text' : var}
        #Checking is max depth is reached
        if(cnt<self.depth):

            #Iterating through every link
             for nextpage in response.css('a::attr(href)'):
                 nextpage = nextpage.get()
                 if nextpage is not None:
                     #print('THE URL IS '+response.urljoin(nextpage))
                     yield scrapy.Request(response.urljoin(nextpage),callback=self.parse, cb_kwargs=dict(cnt = cnt+1,root_url = root_url))  
                    

#Begins the crawlng process in a seperate reactor thread using Crochet
@run_in_reactor
def begin_crawl(URLS,height):
    process = CrawlerRunner(settings={
    "FEEDS": {"scrapped.json": {"format": "json"},},
    "DEPTH_PRIORITY" : 1,
    "SCHEDULER_DISK_QUEUE" : 'scrapy.squeues.PickleFifoDiskQueue',
    'SCHEDULER_MEMORY_QUEUE' : 'scrapy.squeues.FifoMemoryQueue',

    })
    p = process.crawl(nonhtml_spider,urls = URLS,depth = height)


#Sets up the reactor and calls the crawler
def start_crawl(URLS,height):
    setup()
    begin_crawl(URLS=URLS,height=height)

                    
