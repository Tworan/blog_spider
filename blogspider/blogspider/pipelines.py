# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import BlogUser

class BlogspiderPipeline:
    def process_item(self, item, spider):
        if BlogUser.table_exists() == False:
            BlogUser.create_table()
        BlogUser.create(verified_reason=item['verified_reason'], follows_counts=item['follows_counts'], description=item['description'], text=item['text'])
        
        return item
