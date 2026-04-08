import scrapy


class AptekaMdSpider(scrapy.Spider):
    name = "apteka_md"

    def start_requests(self):
        urls = [
            'https://www.apteka.md/category/vitamine',
            'https://www.apteka.md/category/plante-medicinale',
            'https://www.apteka.md/category/produse-igienice',
            'https://www.apteka.md/category/tehnica-medicala',
            'https://www.apteka.md/category/mama-si-copilul',
            'https://www.apteka.md/category/produse-ortopedice',
            'https://www.apteka.md/category/cosmetica',
            'https://www.apteka.md/category/medicamente',
            'https://www.apteka.md/category/nursing-ingrijirea-bolnavilor',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        product_table = response.css("div[class*='mt-6 mb-10 grid gap-x-6 gap-y-10 grid-cols-1 "
                                     "lg:grid-cols-2 xl:grid-cols-4']")
        for product in product_table.css("a"):
            title = product.xpath(
                ".//div[contains(@class, 'line-clamp-3') and contains(@class, 'font-semibold')]/text()").get()
            try:
                price = product.xpath(".//div[contains(@class, 'text-xl') and contains(@class, 'font-semibold')]/text()").get().replace("Lei", "").strip()
            except:
                price = None

            link = "https://www.apteka.md/" + product.css("a").attrib["href"]
            img = product.css("img::attr(src)").get()
            manufacturer = product.xpath(".//div[contains(@class, 'text-xs') and contains(@class, 'font-normal')]/text()").get()

            yield {
                "title": title,
                "price": price,
                "link": link,
                "img": img,
                "manufacturer": manufacturer,
            }

        next_page = response.css("a[aria-label='Go to next page']::attr(href)").get()
        page_param = '?page='
        if next_page:
            if page_param in response.url:
                link_parts = response.url.split(page_param)
                next_page = link_parts[0] + next_page
            else:
                next_page = response.url + next_page

            yield scrapy.Request(url=next_page, callback=self.parse)

