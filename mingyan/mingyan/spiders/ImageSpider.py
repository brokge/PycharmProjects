import scrapy

from mingyan.items import ImagespiderItem


class ImagespiderSpider(scrapy.Spider):
    name = "ImgSpider"

    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ["http://lab.scrapyd.cn/archives/55.html",
                  'http://lab.scrapyd.cn/archives/57.html',
                  ]

    def parse(self, response):
        item = ImagespiderItem()
        imgurls = response.css('.post img::attr(src)').extract()
        item["imgurl"] = imgurls
        item["imgname"] = response.css(".post-title a::text").extract_first()
        yield item
        pass
