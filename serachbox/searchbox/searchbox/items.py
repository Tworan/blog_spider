# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from peewee import *
import scrapy

db = MySQLDatabase("test", host='120.55.64.125', port=25565, user='blog_spider', passwd='123456', charset='utf-8')
class SearchboxItem(scrapy.Item):
    text = scrapy.Field(serializer=str)

class SearchResult(Model):
    text = CharField(verbose_name="text", max_length=1000, null=False)
    class Meta:
        database = db
