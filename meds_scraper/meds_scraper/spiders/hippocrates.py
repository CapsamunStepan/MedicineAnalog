import scrapy


class HippocratesSpider(scrapy.Spider):
    name = "hippocrates"

    def start_requests(self):
        urls = [
            'https://hippocrates.md/ro/catalog/medicamente?show_by=60',
            'https://hippocrates.md/ro/catalog/mama_si_copilul?show_by=60',
            'https://hippocrates.md/ro/catalog/cosmetica_si_igiena?show_by=60',
            'https://hippocrates.md/ro/catalog/vitamine_si_suplimente?show_by=60',
            'https://hippocrates.md/ro/catalog/echipament_medical?show_by=60',
            'https://hippocrates.md/ro/catalog/cuplu_si_sex?show_by=60',
            'https://hippocrates.md/ro/catalog/produse_non-medicale?show_by=60'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        product_table = response.css("div.result-search__content.content-result-search")
        for product in product_table.css("div.content-result-search__item.item-product"):
            price = product.css("div.item-product__price span::text").get()
            # если нет цены продукта нет в наличии, пропуск итерации
            if not price:
                continue
            title = product.css("a[class='item-product__name']::text").get()
            link = 'https://hippocrates.md/' + product.css("a[class='item-product__name']::attr(href)").get()
            img = 'https://hippocrates.md/' + product.css("img::attr(src)").get()
            manufacturer = product.css("p.item-product__brand::text").get()

            yield {
                "title": title,
                "price": price,
                "link": link,
                "img": img,
                "manufacturer": manufacturer,
            }
        next_page = response.xpath('//div[@class="pagging__arrow"]/a[span[text()="Далее"]]/@href').get()
        if next_page:
            next_page = 'https://hippocrates.md' + next_page
            yield scrapy.Request(next_page, callback=self.parse)
