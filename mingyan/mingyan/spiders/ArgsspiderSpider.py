#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class ArgsspiderSpider(scrapy.Spider):
    name = "argsSpider"
    def start_requests(self):
        url = "http://lab.scrapyd.cn/"
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/'+tag

        self.log('url: %s' % url)
        yield scrapy.Request(url, self.parse)


    def parse(self, response):
        mingyan = response.css('div.quote')
        for v in mingyan:
            text = v.css('.text::text').extract_first()
            tags = v.css('.tags .tag::text').extract()
            tags = ','.join(tags)
            file_name = '%s-语录.txt' % tags
            with open(file_name, "a+") as f:
                f.write(text)
                f.write('\n')
                f.write('标签：'+tags)
                f.write('\n----\n')
                f.close()

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

