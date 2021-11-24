import scrapy
from ..items import TurotialItem
# class QuoteSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = [
#        'https://www.dhakatribune.com/world/2021/11/03/bbc-hasina-among-5-to-impact-cop26-outcomes'
#     ]
#
#
#
#
#
#     def parse(self, response):
#
#         items = TurotialItem()
#
#         for text in response.css('::text'):
#             title = text.get().strip()
#
#             if len(title) is not 0:
#                 items['texts'] = title
#                 items['len'] = len(title)
#
#                 yield items
#
#
#
#         #
#         #
#         # next_page = response.css('li.next a::attr(href)').get()
#         #
#         # if next_page is not None:
#         #     yield response.follow(next_page, callback=self.parse)

class testspider(scrapy.Spider):
    name = "testspider"

    # DEPTH_PRIORITY = 1
    # SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
    # SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def start_requests(self):
        return [scrapy.Request('http://localhost/Crawl_check/p1.html', callback=self.parse, cb_kwargs=dict(cnt=1))]

    def parse(self, response, cnt):

        items = TurotialItem()

        #yield {'url': response.url, 'depth': cnt}

        print('THE CURRENT URL IS ' + response.url)

        for txt in response.css("::text"):
            var = txt.get().strip()
            if len(var) != 0:
                #yield {'text': var}
                items['texts'] = var
                items['len'] = cnt

                yield items

        if (cnt < 4):

            for nextpage in response.css('a::attr(href)'):
                nextpage = nextpage.get()
                if nextpage is not None:
                    print('THE URL IS ' + response.urljoin(nextpage))
                    yield scrapy.Request(response.urljoin(nextpage), callback=self.parse, cb_kwargs=dict(cnt=cnt + 1))
