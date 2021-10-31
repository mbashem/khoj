import scrapy

class PostSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        

    ]

    def parse(self,response):
        for post in response.css('::text'):
            var = post.get().strip()
            if len(var) != 0:
                 yield {'text' : var.strip(),
                    'len' : len(var)}
           
            


        