import scrapy


class AptekaMdSpider(scrapy.Spider):
    name = "apteka_md"

    def start_requests(self):
        urls = [
            'https://www.apteka.md/category/cosmetica?page=20',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        product_table = response.css("div[class*='mt-2 mb-10 grid grid-cols-2 md:grid-cols-2 "
                                     "lg:grid-cols-4 xl:grid-cols-6 gap-x-6 gap-y-10']")
        for product in product_table.css("a"):
            title = product.css("div.ProductItem_product__item__title__LiZJy.line-clamp-3.mb-1::text").get()

            try:
                price = product.css("div.ProductItem_product__item__price__VFxS7.mb-2::text").get().replace(" Lei", "")
            except:
                return

            link = "https://www.apteka.md/" + product.css("a").attrib["href"]
            img = product.css("div.h-44.object-contain img::attr(src)").get()
            manufacturer = product.css("div[class*='ProductItem_product__item__manufacturer__NEnGZ h-[1,125rem] "
                                       "line-clamp-1']::text").get()

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

