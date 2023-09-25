import re

from itemloaders.processors import Identity, Join, MapCompose, TakeFirst
from scrapy.loader import ItemLoader


def remove_g(text):
    return text.replace(" g", "").replace(" ", "")


class ProductLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

    scraping_date_in = MapCompose()
    ingredients_in = MapCompose(str.capitalize)
    ingredients_out = Join(" ")
    grams_in = MapCompose(remove_g)    
    product_image_out = Identity()
