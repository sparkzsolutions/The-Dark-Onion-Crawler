# based on https://doc.scrapy.org/en/latest/intro/tutorial.html

import scrapy
import requests


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            print('\n\nurl:', url)
      # use one of the yield below

            # middleware will process the request
            #yield scrapy.Request(url=url, callback=self.parse)

            # check if Tor has changed IP
            yield scrapy.Request('http://icanhazip.com/', callback=self.parse)

    def parse(self, response):
        print('\n\nSpider: Start')
        print("My IP is : " + str(response.body))
        print('Is proxy in response.meta?: ', response.meta)
        print("user_agent is: ", response.request.headers['User-Agent'])
        print('\n\n Spider: End')
