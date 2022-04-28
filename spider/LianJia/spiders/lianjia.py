import scrapy
from ..items import LianjiaItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    # allowed_domains = ['www.lianjia.com']

    def start_requests(self):
        url = 'https://cq.lianjia.com/ershoufang/pg{}/'
        for i in range(1, 3):
            page_url = url.format(i)
            yield scrapy.Request(url=page_url, callback=self.parse)

    def parse(self, response):
        li_list = response.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        for li in li_list:
            detail_url = li.xpath('.//div[@class="title"]/a/@href').extract_first()
            if detail_url:
                yield scrapy.Request(url=detail_url, callback=self.parse_detail)

    def parse_detail(self, response):
        title = response.xpath('//div[@class="title"]/h1/text()').extract_first()
        house_type = response.xpath('//div[@class="room"]/div[1]/text()').extract_first()
        area = response.xpath('//div[@class="area"]/div[1]/text()').extract_first()
        total_price = response.xpath('//div[@class="content"]/div[@class="price-container"]/text()').extract_first()
        item = LianjiaItem()
        item['title'] = title
        item['house_type'] = house_type
        item['area'] = area
        item['total_price'] = total_price
        yield item

