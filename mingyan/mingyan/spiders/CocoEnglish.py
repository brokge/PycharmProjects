#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class itemspider(scrapy.Spider):
    name = "CocoEnglish"
    allowed_domains = ["www.kekenet.com"]
    start_urls = ['http://www.kekenet.com/Article/200707/15846.shtml']

    def parse(self, response):
        mingyan = response.css('#article span p')
        print(len(mingyan))
        if len(mingyan) > 0:
            title = mingyan[0].css('strong::text').extract_first()
            if title.strip() != '':
                content = '' 
                for v in mingyan:
                    content1 = v.css('::text').extract_first()
                    #author = v.css('.author::text').extract_first()
                    #tags = v.css('.tags .tag::text').extract()
                    #tags = ','.join(tags)
                    content += content1
                    content += '\n\n'
                filename = 'coco/%s.txt' % title
                with open(filename, "a+") as f:
                    f.write(content)
                    f.close()
        
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not none:
            """
            如果是相对路径，如：/page/1
            urljoin能替我们转换为绝对路径，也就是加上我们的域名
            最终next_page为：http://lab.scrapyd.cn/page/2/
            """
            next_page = response.urljoin(next_page)
            """
            接下来就是爬取下一页或是内容页的秘诀所在：
            scrapy给我们提供了这么一个方法：scrapy.request()
            这个方法还有许多参数，后面我们慢慢说，这里我们只使用了两个参数
            一个是：我们继续爬取的链接（next_page），这里是下一页链接，当然也可以是内容页
            另一个是：我们要把链接提交给哪一个函数(callback=self.parse)爬取，这里是parse函数，也就是本函数
            当然，我们也可以在下面另写一个函数，比如：内容页，专门处理内容页的数据
            经过这么一个函数，下一页链接又提交给了parse，那就可以不断的爬取了，直到不存在下一页
            """
            yield scrapy.request(next_page, callback=self.parse)
       
