import scrapy

class postsSpider(scrapy.Spider):
    name = 'posts'
    start_urls = [
        'https://www.dhakatribune.com/',
        # 'https://blog.scrapinghub.com/page/2/'
    ]


    def parse(self, response):
        for post in response.css('::text'):
            var = post.get().strip()

            if len(var) != 0:
                yield {
                    'text' : var.strip(),
                    'len' : len(var)
                }

