import scrapy


class ContentSpider(scrapy.Spider):
    name = "content"
    allowed_domains = ["www.fullhdfilmizlesene.pw"]
    start_urls = ["https://www.fullhdfilmizlesene.pw/film/bir-bucuk-gun/"]

    def parse(self, response):
        yield {
            'href':response.css('div.izle-titles a::attr(href)').get()
        }
