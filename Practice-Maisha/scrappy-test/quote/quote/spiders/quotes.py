import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'TitleText': title}
