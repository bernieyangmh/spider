# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

class SpiderYItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img = Field()
    name = Field()


def filter_price(value):
    if value.isdigit():
        return value


class Example(scrapy.Item):
    name = scrapy.Field(
            input_processor=MapCompose(unicode.title),
            output_processor=Join(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, filter_price),
        output_processor=TakeFirst(),
    )

# eg: ItemLoader(item=Product()).add_value('price', [u'&euro;', u'<span>1000</span>'])


# length_out = MapCompose(parse_length, unit='cm') or  loader = ItemLoader(product, unit='cm')
# or ItemLoader(product).context['unit'] = 'cm' to change loader_context
# def parse_length(text, loader_context):
#     unit = loader_context.get('unit', 'm')
#     parsed_length = 'some parsing'
#     return parsed_length
