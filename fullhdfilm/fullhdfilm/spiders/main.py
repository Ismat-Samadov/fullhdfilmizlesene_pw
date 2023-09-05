import scrapy


class CombinedSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["fullhdfilmizlesene.pw"]
    start_urls = ["https://fullhdfilmizlesene.pw"]

    def parse(self, response):
        # Follow film links and scrape data
        film_links = response.css('a.tt::attr(href)').getall()

        for film_link in film_links:
            yield scrapy.Request(url=film_link, callback=self.parse_film)

        # Follow pagination links
        next_page = response.css('div.sayfalama a.ileri::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_film(self, response):
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
            'tags': response.css('li span.dt ~ div.sag.etiket::text').getall()
        }
