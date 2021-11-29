import scrapy
from scrapy.crawler import CrawlerProcess


class testspider(scrapy.Spider):

    name = "testspider"
   
    DEPTH_PRIORITY = 1
    SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
    SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

    start_urls = [
            'https://quotes.toscrape.com/page/1/'
    ]
    

    def start_requests(self):
        return [scrapy.Request('http://localhost/Crawl_check/p1.html',callback=self.parse, cb_kwargs=dict(cnt = 1))]

         

    def parse(self,response,cnt):

        
        yield {'url' : response.url,'depth' : cnt}
        print('THE CURRENT URL IS '+response.url)

        for txt in response.css("::text"):
            var = txt.get().strip()
            if len(var) != 0:
                yield {'text' : var}
         


        if(cnt<10):

             for nextpage in response.css('a::attr(href)'):
                 nextpage = nextpage.get()
                 if nextpage is not None:
                     print('THE URL IS '+response.urljoin(nextpage))
                     yield scrapy.Request(response.urljoin(nextpage),callback=self.parse, cb_kwargs=dict(cnt = cnt+1))  
                     


process = CrawlerProcess(settings={
    "FEEDS": {
        "scrapped.json": {"format": "json"},
    },
})


process.crawl(testspider)
print("Starting crawl")
process.start()
print("Crawl ended")
                    


            


