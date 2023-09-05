import scrapy


class ContentSpider(scrapy.Spider):
    name = "content"
    allowed_domains = ["www.fullhdfilmizlesene.pw"]
    start_urls = ["https://www.fullhdfilmizlesene.pw/film/bir-bucuk-gun/"]

    def parse(self, response):
        yield {
            'name': response.css('.izle-titles h1 a::text').get(),
            'href': response.css('div.izle-titles a::attr(href)').get(),
            'imdb': response.css('.header-sag .imdb-ic span::text').get(),
            'score': response.css('.header-sag .puanx-ic .puanx-puan::text').getall()[1],
            'description': response.css('div.film-ozeti div.ozet-ic p::text').getall(),
            'director': response.css('div.dd a span::text').get(),
            'actors': response.css('div.dd a span::text').getall(),
            'category': response.css('div.dd a.category::text').get(),
            'genres': response.css('div.dd a[rel="category tag"]::text').getall(),
            'tags':response.css('li span.dt ~ div.sag.etiket::text').getall()
        }
