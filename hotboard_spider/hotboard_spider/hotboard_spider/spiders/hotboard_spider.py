import scrapy
from hotboard_spider.items import *
class HotBoard(scrapy.Spider):
    '''
    hotboard_url: 热榜的url
    web: 爬取热榜的网站名称
    internal_url_dict: 程序内置各大网站的热榜爬取url
    '''
    name = 'hb'
    hotboard_url = 'https://www.baidu.com'
    start_urls = [hotboard_url, ]
    web = ['bilibili', '知乎', '微博']
    internal_url_dict = {
        '微博': 'https://tophub.today/n/KqndgxeLl9',
        '知乎': 'https://tophub.today/n/mproPpoq6O',
        'bilibili': 'https://tophub.today/n/74KvxwokxM'
    }
    i = -1

    def parse(self, response):
        #* 伪装爬虫
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        #* 这里的url改成网址 到时候把网址存在字典里
        while self.i < 2:
            self.i += 1
            yield scrapy.Request(url = self.internal_url_dict[self.web[self.i]], headers = headers, callback = self.get_hotboard)
            

    def get_hotboard(self, response):
        hotboard_items = HotboardSpiderItem()
        hotboard_items['hot_board'] = response.xpath('//div[@id="page" and @class="page"]/div[contains(@class, "c-d")]/div[@class="Zd-p-Sc"]/div[@class="cc-dc"]/div[@class="cc-dc-c"]/div[@class="jc"]/div[@class="jc-c"]/table[@class="table"]/tbody/tr/td[@class="al"]/a/text()').getall()
        hotboard_items['plat'] = response.xpath('normalize-space(//div[@id="page" and @class="page"]/div[contains(@class, "c-d")]/div[@class="zb-p"]/div[@class="Xc-ec"]/div[contains(@class, "Xc-ec-Zc") and @id="tabbed-header-panel"]/div[@class="Xc-ec-ad"]/div[contains(@class, "b-L")]/text())').extract()

        yield hotboard_items
