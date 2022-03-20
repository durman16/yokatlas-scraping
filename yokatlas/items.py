# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from re import S
import scrapy


class YokatlasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    university_code = scrapy.Field()

    university_type = scrapy.Field()

    university = scrapy.Field()

    faculty = scrapy.Field()

    point_type = scrapy.Field()

    total_quota = scrapy.Field()

    total_placed = scrapy.Field()

    placed_rate = scrapy.Field()

    settled_unregistered = scrapy.Field()

    ceiling_order = scrapy.Field()

    base_order = scrapy.Field()

    pass
