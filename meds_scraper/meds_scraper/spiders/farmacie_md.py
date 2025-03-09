import scrapy


class MedsSpider(scrapy.Spider):
    name = "farmacie_md"

    def start_requests(self):
        urls = [
            'https://farmacie.md/ro/cosmetica',
            'https://farmacie.md/ro/mama-si-copilul',
            'https://farmacie.md/ro/produse-de-igiena',
            'https://farmacie.md/ro/medicina-naturista',
            'https://farmacie.md/ro/scutece-si-protectoare',
            'https://farmacie.md/ro/produse-parafarmaceutice',
            'https://farmacie.md/ro/raceala-si-gripa',
            'https://farmacie.md/ro/antineoplazice-si-imunomodulatoare',
            'https://farmacie.md/ro/aparatul-respirator',
            'https://farmacie.md/ro/digestie-si-metabolism',
            'https://farmacie.md/ro/produse-antiparazitare',
            'https://farmacie.md/ro/sistemul-nervos-central',
            'https://farmacie.md/ro/sistemul-cardiovascular',
            'https://farmacie.md/ro/preparate-dermatologice',
            'https://farmacie.md/ro/sistemul-musculo-scheletic',
            'https://farmacie.md/ro/antiinfectioase-de-uz-sistemic',
            'https://farmacie.md/ro/sange-si-organe-hematopoetice',
            'https://farmacie.md/ro/organe-senzitive-ochi-si-urechi',
            'https://farmacie.md/ro/aparat-genito-urinar-si-hormoni-sexuali',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for product in response.css('div.product-cart__inner'):
            lei = product.css("span.product-cart__price-new--lei::text").get()
            if lei:
                ban = product.css("span.product-cart__price-new--ban::text").get()
                price = lei + "," + ban
            else:
                return

            """
            -товар без цены означает, что его нет в наличии
            -товары отсортированы так, что сначала идут товары в наличии, а затем которых нет в наличии
            -если начались товары, которых нет в наличии, то можно прервать парсинг
            -это сэкономит время, и поможет избежать лишней работы
            """

            yield {
                "name": product.css("h3.product-cart__title::text").get().strip(),
                "price": price,
                "url": "https://farmacie.md" + product.css("a.product-cart__image").attrib['href'],
                "image": product.css("a.product-cart__image img::attr(src)").get(),
            }

        page_param = '?page='
        if page_param in response.url:
            link_parts = response.url.split(page_param)
            current_page = int(link_parts[-1])
            next_page = link_parts[0] + page_param + str(current_page + 1)
        else:
            next_page = response.url + page_param + '2'

        yield response.follow(next_page, callback=self.parse)
