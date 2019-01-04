#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class itemSpider(scrapy.Spider):
    name = "itemSpider"
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        v = response.css('div.quote')[0]
        text = v.css('.text::text').extract_first()
        author = v.css('.author::text').extract_first()
        tags = v.css('.tags .tag::text').extract()
        tags = ','.join(tags)
        """
        接下来进行写文件操作，每个名人的名言储存在一个txt文档里面
        """
        fileName = '%s-语录.txt' % author
        with open(fileName, "a+") as f:
             f.write(text)
             f.write("\n")
             f.write("标签：" + tags)
             f.write("\n-------\n")
             f.close()
