import scrapy

class LightingSpider(scrapy.Spider):
    name = "lighting"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        products = response.css("div[data-testid='product-card']")
        print("🔍 Найдено товаров:", len(products))

        for product in products:
            title = product.css("span[itemprop='name']::text").get()
            price = product.css("span[data-testid='price']::text").get()
            url = product.css("a::attr(href)").get()

            if url and not url.startswith("http"):
                url = response.urljoin(url)

            yield {
                "title": title.strip() if title else None,
                "price": price.strip() if price else None,
                "url": url
            }

        # Пагинация
        next_page = response.css("a[data-testid='pagination-forward']::attr(href)").get()
        if next_page:
            print("➡️ Следующая страница:", next_page)
            yield response.follow(next_page, callback=self.parse)
