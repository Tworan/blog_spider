# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import HotBoard

class HotboardSpiderPipeline:
    def process_item(self, item, spider):
        if HotBoard.table_exists() == False:
            HotBoard.create_table()
        HotBoard.create(hot_board=item['hot_board'], plat=item['plat'])
        return item

