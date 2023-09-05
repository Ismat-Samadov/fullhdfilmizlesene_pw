import scrapy


class LinksSpider(scrapy.Spider):
    name = "links"
    allowed_domains = ["fullhdfilmizlesene.pw"]
    start_urls = ["https://fullhdfilmizlesene.pw"]

    def parse(self, response):
        yield {
            'links': response.css('a.tt::attr(href)').getall(),
        }
        next_page = response.css('div.sayfalama a.ileri::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
