import scrapy



class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]



    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()

            yield {
                'title': title,
                'author': author,
                'tags': tags
            }
