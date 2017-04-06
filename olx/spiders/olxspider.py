import scrapy
from olx.items import OlxRealEstate

class OlxSpider(scrapy.Spider):
    name = 'olxspider'
    allowed_domains = ['rj.olx.com.br']

    def start_requests(self):
        """
        """
        yield scrapy.Request('http://rj.olx.com.br/rio-de-janeiro-e-regiao/centro/imoveis/aluguel', self.parse)

    def parse(self, response):
        """
        """
        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse_item)

    def item_url_is_valid(self, url):
        """
        """
        estate_id = url.split('-')[-1]
        try:
            integer = int(estate_id)
            start = url.startswith('http://rj.olx.com.br/rio-de-janeiro-e-regiao/imoveis/')
            return start
        except Exception, e:
            return False

    def parse_item(self, response):
        
#        if self.item_url_is_valid(response.url):

        item = OlxRealEstate()

        item['url'] = response.url
        item['price'] = response.xpath('//div[@class="OLXad-price"]//li[@class="item"]//strong[@class="description"]')
        item['ad_text'] = response.xpath('//div[@class="OLXad-description"]//li[@class="item"]//strong[@class="description"]')

        yield item
