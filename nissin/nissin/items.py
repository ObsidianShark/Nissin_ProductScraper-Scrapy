# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    product_name = scrapy.Field()
    ingredients = scrapy.Field()
    product_image = scrapy.Field()
    about = scrapy.Field()
    grams = scrapy.Field()
    calories = scrapy.Field()

    url = scrapy.Field()
    scraping_date = scrapy.Field()
