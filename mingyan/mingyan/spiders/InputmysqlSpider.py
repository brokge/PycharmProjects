#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
from mingyan.items import ScrapymysqlItem #引入item

class InputmysqlSpider(scrapy.Spider):
    name = "inputMysql"
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = ["http://lab.scrapyd.cn/"]

    def parse(self, response):
        mingyan = response.css('div.quote')

        item = ScrapymysqlItem()

        for  v in mingyan:
            item['cont'] = v.css('.text::text').extract_first()
            tags = v.css('.tags .tag::text').extract()
            item['tag'] = ','.join(tags)
            yield item # 把取到的数据提交给pipline 处理
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse) #提交给parse继续抓取下一页


