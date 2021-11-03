import scrapy
from ..items import TurotialItem
class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
       'https://www.dhakatribune.com/'
    ]

    def parse(self, response):

        items = TurotialItem()

        for text in response.css('::text'):
            title = text.get().strip()

            if len(title) is not 0:
                items['texts'] = title
                items['len'] = len(title)

                yield items



        #
        #
        # next_page = response.css('li.next a::attr(href)').get()
        #
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)


