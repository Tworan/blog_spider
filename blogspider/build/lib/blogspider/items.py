# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from peewee import *
import scrapy
import datetime
db = MySQLDatabase("test", host='120.55.64.125', port=25565, user='blog_spider', passwd='123456', charset='utf8')

#*新加内容
# def make_table_name(model_class):
#     model_name = model_class.__name__
#     return model_name.lower() + '-' + str(datetime.date.today())

class BlogspiderItem(scrapy.Item):
    '''
    test: 动态
    follows_counts: 关注数
    description: 用户描述
    verified_reason: 个人认证
    '''
    text = scrapy.Field(serializer=list)
    follows_counts = scrapy.Field(serializer=str)
    description = scrapy.Field(serializer=str)
    verified_reason = scrapy.Field(serializer=str)
    potential_followings = scrapy.Field(serializer=list)

class BlogUser(Model):
    verified_reason = CharField(verbose_name="verified_reason", max_length=100, null=False)
    follows_counts = CharField(verbose_name="follows_counts", max_length=10, null=False)
    description = CharField(verbose_name="description", max_length=100, null=False)

    class Meta:
        database = db
        # table_function = make_table_name

class Activation(Model):
    text = CharField(verbose_name="text", max_length=10000, null=False)

    class Meta:
        database = db

