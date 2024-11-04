import scrapy

class AllocineSpider(scrapy.Spider):
    name = "allocine"
    start_urls = ['https://www.allocine.fr/film/agenda/']

    def parse(self, response):
        for film in response.css('div.card.entity-card'):
            yield {
                'titre': film.css('h2 a::text').get(),
                'link': film.css('h2 a::attr(href)').get(),
                'release_date': film.css('span.date::text').get(),
                'image': film.css('img::attr(src)').get(),
            }

        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)