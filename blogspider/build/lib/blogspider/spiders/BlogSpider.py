import scrapy, json, sys, requests, re, os
from urllib.parse import urlencode
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from blogspider.items import *
class BlogSpider(scrapy.Spider):
    
    '''
    name: 爬虫的名称
    ID: 爬取用户的昵称

    搜索接口: https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D[想要搜索的内容]&page_type=searchall
    '''
    name = 'bs'
    ID = 'bilibili'

    #* ~%3D ID &page_~
    start_urls = ['https://m.weibo.cn/api/container' + \
                  '/getIndex?containerid=100103type%3D1%26q%3D' + str(ID) + '&page_type=searchall']
    month = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05', 
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sept': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
    }
    relevant_uid = None

    def parse(self, response):
        #* 匹配uid
        uid = str(json.loads(response.text)['data']['cards'][0]['card_group'][0]['user']['id'])
        #* relevant_uid为相关用户的uid
        self.relevant_uid = [str(json.loads(response.text)['data']['cards'][0]['card_group'][1]['elements'][i]['uid']) for i in range(4)]
        url = 'https://m.weibo.cn/api/container/getIndex?'
        #* pages为爬取的页数
        paras = {
                    'uid': uid,
                    't': '0',
                    'luicode': '10000011',
                    'lfid': '100103type=1&q=' + self.ID,
                    'type': uid,
                    'value': uid,
                    'containerid': '107603' + uid,
                    'page_type': '60',
                    'page': '1'
                }
        #* 伪装爬虫
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

        #* 爬取动态文本
        yield scrapy.Request(url = url + urlencode(paras), callback = self.get_text, headers = headers)    


    def get_text(self, response):
        blog_items = BlogspiderItem()
        response_json_format = json.loads(response.text)
        final_text = ''
        #* 8为获取的条数
        for i in range(10):
            # print(json.loads(response.text)['data']['cards'][i]['mblog']['text'])
            temp_text = response_json_format['data']['cards'][i]['mblog']['text']
            temp_time = response_json_format['data']['cards'][i]['mblog']['created_at'].split(' ')
            time = temp_time[5] + '-' + self.month[temp_time[1]] + '-' + temp_time[2]
            final_text = final_text + re.sub('<.*?>', '', temp_text) + '//' + time + '//@@//'
        blog_items['potential_followings'] = self.relevant_uid
        blog_items['follows_counts'] = response_json_format['data']['cards'][0]['mblog']['user']['followers_count']
        blog_items['description'] = response_json_format['data']['cards'][0]['mblog']['user']['description']
        blog_items['verified_reason'] = response_json_format['data']['cards'][0]['mblog']['user']['verified_reason']
        blog_items['text'] = final_text
    
        yield blog_items