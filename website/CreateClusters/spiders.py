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
import fitz
import urllib.request
from io import BytesIO
import time


class main_spider(scrapy.Spider):

    name = "main_spider"
   
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
    
    def follow_links(self,response,cnt,root_url):
        for nextpage in response.css('a::attr(href)'):
             nextpage = nextpage.get()
             if nextpage is not None:
                 yield scrapy.Request(response.urljoin(nextpage),callback=self.parse, cb_kwargs=dict(cnt = cnt+1,root_url = root_url))

               
    #This is the callback function used to process the response
    def parse(self,response,cnt,root_url):
        pass
            

#This is the crawler class for collecting nonhtml data
class nonhtml_spider(main_spider):

    name = "nonhtml_spider"

    #This is the callback function used to process the response
    def parse(self,response,cnt,root_url):
        
        yield {'url' : response.url,'depth' : cnt}

        for txt in response.css("::text"):

            var = txt.get().strip()

            if len(var) != 0:
                #If the text is not empty we insert it into solr
                indexer.insert.insert_into_solr_text( var, cnt, root_url, response.url, "nonhtml")
                yield {'text' : var}

        #Follow links if max depth not reached
        if(cnt<self.depth):
            yield from self.follow_links(response,cnt,root_url)
            

#This is the crawler class for collecting pdf data
class pdf_spider(main_spider):

    name = "pdf_spider"

    def ispdf(self,str):
        str  = str.split('.')
        if(len(str)!=0 and str[-1]=='pdf'):
            return True
        else:
            return False
    
    def getPdf(self,link):
        data = urllib.request.urlopen(link)

        data = BytesIO(data.read())

        pdf_file = fitz.open(stream = data , filetype = "pdf")

        str = ""
        for pages in pdf_file:
            str += pages.get_text()
    
        return str



    def parse(self,response,cnt,root_url):
        
        yield {'url' : response.url,'depth' : cnt}
        
        if(self.ispdf(response.url)):
            yield {'pdf':response.url,'depth':cnt}
            txt = self.getPdf(response.url)
            yield{'pdf text' : txt}
            indexer.insert.insert_into_solr_text(txt, cnt, root_url, response.url, "pdf")
        

        if(cnt<self.depth):
            yield from self.follow_links(response,cnt,root_url)




                    

#Sets up the reactor and calls the crawler for strategy: nonhtml text
def run_nonhtmlspider(URLS,height):
    setup()
    begin_crawl(nonhtml_spider,URLS=URLS,height=height)

#Sets up the reactor and calls the crawler for strategy: pdf text
def run_pdfspider(URLS,height):
    setup()
    begin_crawl(pdf_spider,URLS=URLS,height=height)

#Begins the crawlng process in a seperate reactor thread using Crochet
@run_in_reactor
def begin_crawl(spider,URLS,height):
    process = CrawlerRunner(settings={
    "FEEDS": {"scrapped.json": {"format": "json"},},
    "DEPTH_PRIORITY" : 1,
    "SCHEDULER_DISK_QUEUE" : 'scrapy.squeues.PickleFifoDiskQueue',
    'SCHEDULER_MEMORY_QUEUE' : 'scrapy.squeues.FifoMemoryQueue',

    })
    p = process.crawl(spider,urls = URLS,depth = height)
    #p.addBoth(lambda _: reactor.stop())
    #reactor.run()
    




