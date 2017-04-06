import scrapy
from olx.items import OlxRealEstate

class OlxSpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']

    def start_requests(self):
        """
        """
        yield scrapy.Request('http://www.example.com/1.html', self.parse)
        yield scrapy.Request('http://www.example.com/2.html', self.parse)
        yield scrapy.Request('http://www.example.com/3.html', self.parse)

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
        
        if self.item_url_is_valid(response.url):

            item = OlxRealEstate()

            item['estate_id'] = int(estate_id)
            item['url'] = response.url
            item['price'] = response.xpath('//div[@class="OLXad-price"]//li[@class="item"]//strong[@class="description"]')
            item['ad_text'] = response.xpath('//div[@class="OLXad-description"]//li[@class="item"]//strong[@class="description"]')
"""
            details_keys = response.xpath('//div[@class="OLXad-details"]//li[@class="item"]//span[@class="term"]')
            details_values = response.xpath('//div[@class="OLXad-details"]//li[@class="item"]//strong[@class="description"]')
            details = zip(details_keys, details_values)

            location_keys = response.xpath('//div[@class="OLXad-location-map"]//li[@class="item"]//span[@class="term"]')
            location_values = response.xpath('//div[@class="OLXad-location-map"]//li[@class="item"]//strong[@class="description"]')
            location = zip(location_keys, location_values)

            info = {}

            info['features'] = response.xpath('//div[@class="OLXad-features"]//li[@class="item"]//strong[@class="description"]')
            info['phone'] = response.xpath('')

            info['area'] = details[""]
            info['fees'] = details[""]
            info['taxes'] = details[""]
            info['longitude'] = location[""]
            info['latitude'] = location[""]
            info['district'] = location[""]
            info['zipcode'] = location[""]
            
            item['info'] = info
"""

            yield item

