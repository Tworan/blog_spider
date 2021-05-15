# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from peewee import *
from urllib.parse import scheme_chars
import scrapy
db = MySQLDatabase("test", host='120.55.64.125', port=25565, user='blog_spider', passwd='123456', charset='utf8')

class HotboardSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hot_board = scrapy.Field() 
    plat = scrapy.Field()

class HotBoard(Model):
    hot_board = CharField(verbose_name="hot_board", max_length=10000)
    plat = CharField(verbose_name="plat", max_length=20)

    class Meta:
        database = db