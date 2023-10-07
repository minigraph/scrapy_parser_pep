import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_td = response.css('td')
        all_peps = all_td.css('a.pep.reference.internal::attr(href)')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': int(
                response.css(
                    'link[rel=canonical]'
                ).css('link::attr(href)').re(r'\d{4}')[0]),
            'name': response.css('h1.page-title::text').get(),
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
