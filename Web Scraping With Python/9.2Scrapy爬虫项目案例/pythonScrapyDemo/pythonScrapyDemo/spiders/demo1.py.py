# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo1'  # 名字
    # allowed_domains = ['python123.io']      # 起启域名
    start_urls = ['http://python123.io/ws/demo.html']   # 要爬取的网址

    def parse(self, response):              # parse用于处理响应，解析内容形成字典，发现新的URL爬取请求
        fname=response.url.splie('/')[-1]
        with open(fname,'wb') as f:
            f.write(response.body)
        self.log('Saving file %s.'%fname)                          # 运行日志
