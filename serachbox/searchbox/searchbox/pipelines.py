# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import SearchResult

class SearchboxPipeline:
    def process_item(self, item, spider):
        if SearchResult.table_exists() == False:
            SearchResult.create_table()