import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
from urllib.parse import urldefrag
import re
from urllib.parse import urlparse, urlunparse
from urllib.parse import urlencode
#import pyodbc
# from fast_to_sql import fast_to_sql as fts

#API_KEY = '59945cf2-4029-4350-9d08-d659153f931f'

#def get_scrapeops_url(url):
 #   payload = {'api_key': API_KEY, 'url': url}
  #  proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
   # return proxy_url

class JanJapanSpider(scrapy.Spider):
    name = 'JanJapan'


    start_urls = [
        'https://janjapan.com/used-car/safrica-durban/mercedes/c-class/871517#car_detail_gsllary'
    ]
    f_lst = []
    items =[]

    def parse(self, response):

        items = {

            'StockId':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/div[1]/h5/text()').get(),
            'chassis':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[1]/li[1]/span[2]/text()').get(),
            'Model':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[1]/li[2]/span[2]/text()').get(),
            'Engine Capacity':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[1]/li[3]/span[2]/text()').get(),
            'Drive Type':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[1]/li[4]/span[2]/text()').get(),
            'Transmission':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[1]/li[5]/span[2]/text()').get(),
            'Port':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[1]/li[7]/span[2]/text()').get(),
            'Sale Location':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[1]/li[8]/span[2]/text()').get(),
            'Grade/Class':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[1]/li[9]/span[2]/text()').get(),
            'Mileage':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[2]/li[1]/span[2]/text()').get().strip(),
            'Steering':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[2]/li[2]/span[2]/text()').get(),
            'Engine Code':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[2]/li[3]/span[2]/text()').get(),
            'Color':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[2]/li[4]/span[2]/text()').get().strip(),
            'Interior Color':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[2]/li[5]/span[2]/text()').get().strip(),
            'Fuel Type':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[2]/li[6]/span[2]/text()').get(),
            'Seats':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[2]/li[7]/span[2]/text()').get(),
            'Doors':response.xpath('//*[@id="car_individual_detail"]/div[6]/div[1]/div[1]/div[3]/ul[2]/li[8]/span[2]/text()').get(),
            'Total Views':response.xpath('//*[@id="car_detail_gsllary"]/div[2]/div[4]/div[1]/p/span[2]/text()').get(),

            'source' : 'Janjapan',








            }

        JanJapanSpider.items.append(items)


        lnks = pd.read_csv('lk.csv')
        lnks= lnks.dropna()
        lks = lnks['link_name'].values.tolist()
        lks1=lks


        for i in lks1:
            new_url=i



            #next_page=str(next_page)


            yield scrapy.Request(url=new_url,callback=self.parse)

        df = pd.DataFrame(JanJapanSpider.items)

        yield df.to_csv('Janjapnfinal.csv')

        print("Data appended successfully.")

process = CrawlerProcess()
process.crawl(JanJapanSpider)
process.start()
print('crawling complete')
