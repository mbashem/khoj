import scrapy


class testspider(scrapy.Spider):
    name = "testspider"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        

    ]

   
    def start_requests(self):
        return [scrapy.Request('http://quotes.toscrape.com/page/1/',callback=self.parse, cb_kwargs=dict(cnt = 2))]

         

    def parse(self,response,cnt):

         
        yield{'url' : response.url,'depth' : cnt}
       
        yield scrapy.Request('http://quotes.toscrape.com/page/2/',callback=self.parse, cb_kwargs=dict(cnt = cnt+1))
        
        
                
        
            


        