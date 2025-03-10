import scrapy
import json


class FarmaciaFamilieiSpider(scrapy.Spider):
    name = "farmacia_familiei"

    def start_requests(self):
        urls = [
            'https://ff.md/collections/sanatate',
            'https://ff.md/collections/vitamine-si-minerale',
            'https://ff.md/collections/cuplu-si-sex',
            'https://ff.md/collections/frumusete-si-igiena',
            'https://ff.md/collections/dermatocosmetica',
            'https://ff.md/collections/mama-si-copilul',
            'https://ff.md/collections/optica',

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        product_list = response.css("div.product-list.product-list--collection.product-list--with-sidebar")

        for product in product_list.css("div[class*='product-item product-item--vertical']"):
            in_stock = product.css("span[class='product-item__inventory inventory inventory--high']"
                                   "::text").get() == "Disponibil"
            if not in_stock:
                continue
            title = product.css("a[class='product-item__title text--strong link']::text").get()
            link = 'https://ff.md' + product.css("a[class='product-item__title text--strong link']::attr(href)").get()
            price = product.css("span[class*='price']::text").get().replace(' MDL', '')
            manufacturer = product.css("a[class='product-item__vendor link']::text").get()
            widths = product.css("img::attr(data-widths)").get()
            if widths:
                width = json.loads(widths)[-1]
                img = 'https:' + product.css("img::attr(data-src)").get().replace('{width}', str(width))
            else:
                img = 'https://ff.md/cdn/shop/files/105202_600x.webp?v=1734088438'

            yield {
                "title": title,
                "price": price,
                "link": link,
                "img": img,
                "manufacturer": manufacturer,
            }

        next_page = response.css("a[class='pagination__next link']::attr(href)").get()

        if next_page:
            next_page = 'https://ff.md' + next_page
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            return
