from datetime import datetime

from nissin.items import ProductItem
from nissin.itemsloaders import ProductLoader
from scrapy.spiders import SitemapSpider


class ProductsSpider(SitemapSpider):
    name = "products"
    allowed_domains = ["nissinfoods.com"]
    sitemap_urls = ["https://www.nissinfoods.com/sitemap_index.xml"]
    sitemap_rules = [
        ("/product/", "parse_product"),
    ]

    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_DEBUG": True,
        # 'HTTPCACHE_ENABLED': True,
    }

    def parse_product(self, response):
        product = ProductLoader(item=ProductItem(), selector=response)
        product.add_xpath(
            "product_name", "//h1[contains(@class, 'single-product__title')]/text()"
        )
        product.add_xpath(
            "ingredients",
            "//*[@class='single-product__nutritional-facts-popup']//div[@class='single-product__ingredients']//p/text()",
        )
        product.add_xpath(
            "product_image",
            "//div[@class='single-product__gallery des']//div[@class='single-product__gallery-item-image']/img[@data-lazy-src]/@data-lazy-src",
        )
        product.add_xpath(
            "about", "//div/div[@class='single-product__description']/p/text()"
        )
        product.add_xpath(
            "grams",
            "//div[@class='single-product__nutritional-facts']/div[span[contains(text(), 'Serving')]]/p[contains(text(), 'g')]/text()",
        )
        product.add_xpath(
            "calories",
            "//div[@class='single-product__nutritional-facts']/div[span[contains(text(), 'Calories')]]/p/text()",
        )
        product.add_value("url", response.request.url)
        product.add_value("scraping_date", datetime.now())

        yield product.load_item()
