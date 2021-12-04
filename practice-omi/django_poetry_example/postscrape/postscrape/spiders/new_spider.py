import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class crawlspider(CrawlSpider):

    name = 'crawlspider'
    start_urls = ['http://localhost/Crawl_check/p1.html']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        yield {'url': response.url}

        for txt in response.css("::text"):
                var = txt.get().strip()
                if len(var) != 0:
                    yield {'text': var}

        # for nextpage in response.css('a::attr(href)'):
        #             nextpage = nextpage.get()
        #             if nextpage is not None:
        #                 print('THE URL IS ' + response.urljoin(nextpage))
        #                 yield scrapy.Request(response.urljoin(nextpage), callback=self.parse)
