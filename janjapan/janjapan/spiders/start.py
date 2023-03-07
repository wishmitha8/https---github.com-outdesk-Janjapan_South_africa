import scrapy
from scrapy.crawler import CrawlerProcess
import logging
import pandas as pd
import subprocess
import os

class JanJapanSpider(scrapy.Spider):
    name = 'JanJapan'
    #allowed_domains = ['https://janjapan.com']
    #page_number=2


    start_urls = [
                        'https://janjapan.com/stock/location/s.africa%20durban-14/1',

                        ]


        #'https: // janjapan.com / used - cars / all - stock / toyota / all - models / 1'

    def parse(self, response):
        lst_page = response.xpath('//*[@id="pagination-wrap"]/li[14]/a/text()').get()
        # print(int(lst_page[-10:-5])/25)
        lst_page = round(int(lst_page))
        print(lst_page)

        lst = []
        for i in range(1, lst_page + 1):
            next_page_url = "https://janjapan.com/stock/location/s.africa%20durban-14/" + str(i)
            lst.append(next_page_url)

        df = pd.DataFrame(lst)
        df.columns = ['page_links']

        yield df.to_csv('page_links.csv', index=False, header=True)


# Run first Python file


process = CrawlerProcess()
process.crawl(JanJapanSpider)
process.start()
#os.system('Items.py')
#os.system('details.py')


