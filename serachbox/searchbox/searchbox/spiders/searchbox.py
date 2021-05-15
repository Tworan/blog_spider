import scrapy
import re, sys
class SearchBox(scrapy.Spider):
    name = 'sb'
    key_words = '关键字'
    start_urls = ['https://m.weibo.cn/api/container' + \
                  '/getIndex?containerid=100103type%3D1%26q%3D' + str(key_words) + '&page_type=searchall']

    def parse(self, response):
        search_item = SearchItem()
        response_json_format = json.loads(response.text)
        final_text = ''
        #* 8为获取的条数
        for i in range(10): 
            try:
                # print(json.loads(response.text)['data']['cards'][i]['mblog']['text'])
                temp_text = response_json_format['data']['cards'][i]['mblog']['text']
            except:
                continue

            final_text = final_text + re.sub('<.*?>', '', temp_text) + '//@@//'

        search_item['text'] = final_text
        yield search_item