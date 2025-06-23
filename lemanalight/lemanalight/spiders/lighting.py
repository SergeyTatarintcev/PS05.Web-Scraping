import scrapy


class LightingSpider(scrapy.Spider):
    name = "lighting"
    allowed_domains = ["krasnodar.lemanapro.ru"]
    start_urls = ["https://krasnodar.lemanapro.ru"]

    def parse(self, response):
        pass
