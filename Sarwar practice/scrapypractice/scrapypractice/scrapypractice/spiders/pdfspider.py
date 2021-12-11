from crochet import setup,run_in_reactor
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
import fitz
import urllib.request
import requests
from io import BytesIO
import PyPDF2

def ispdf(str):
     str  = str.split('.')
     if(len(str)!=0 and str[-1]=='pdf'):
         return True
     else:
         return False
     

class pdf_spider(scrapy.Spider):

    name = "pdf_spider"
   
    
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
        if(ispdf(response.url)):
            yield {'pdf':response.url,'depth':cnt}

        if(cnt<self.depth):

             for nextpage in response.css('a::attr(href)'):
                 nextpage = nextpage.get()
                 if(nextpage is not None):
                    yield scrapy.Request(response.urljoin(nextpage),callback=self.parse, cb_kwargs=dict(cnt = cnt+1,root_url = root_url))  
                    



def begin_crawl(URLS,height):
    process = CrawlerRunner(settings={
    "FEEDS": {"scrapped.json": {"format": "json"},},
    "DEPTH_PRIORITY" : 1,
    "SCHEDULER_DISK_QUEUE" : 'scrapy.squeues.PickleFifoDiskQueue',
    'SCHEDULER_MEMORY_QUEUE' : 'scrapy.squeues.FifoMemoryQueue',

    })
    p = process.crawl(pdf_spider,urls = URLS,depth = height)
    p.addCallback(lambda _:reactor.stop())
    reactor.run()

data = requests.get("https://papers.gceguide.com/A%20Levels/Mathematics%20(9709)/2021/9709_s21_ms_13.pdf")

data = data.content

data = BytesIO(data)

pdf_file = PyPDF2.PdfFileReader(data)


for i in range(pdf_file.getNumPages()):
    print(pdf_file.getPage(i).extractText())

#begin_crawl(URLS = ['http://www.northsouth.edu/nsu-announcements/'],height = 2)
print("DONE")

#ispdf('http://www.northsouth.edu/nsu-announcements.pdf')


                    
