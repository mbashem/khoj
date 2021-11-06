import scrapy

class postsSpider(scrapy.Spider):
    name = 'posts'
    start_urls = [
        'http://localhost/Crawl_check/p1.html',

    ]

    # def start_requests(self):
    #     return [scrapy.Request('http://localhost/Crawl_check/p1.html', callback=self.parse)]

    def parse(self, response):

        yield {
            'url': response.url,
            # 'depth': cnt
        }

        for link in response.css('a::attr(href)'):
                yield response.follow(link.get(), callback=self.parse_text)


    def parse_text(self, response):

        for post in response.css('::text'):
            var = post.get().strip()

            if len(var) != 0:
                yield {
                    'text' : var,
                    'len' : len(var)
                }



    # def parse(self, response):
    #
    #     yield {
    #         'url' : response.url
    #     }
    #
    #
    #     for post in response.css('::text'):
    #         var = post.get().strip()
    #
    #         if len(var) != 0:
    #             yield {
    #                 'text' : var.strip(),
    #                 'len' : len(var)
    #             }
    #
