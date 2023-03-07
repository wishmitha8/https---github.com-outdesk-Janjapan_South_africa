import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
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
        'https://janjapan.com/stock/location/s.africa%20durban-14/1'
    ]
    f_lst = []
    def parse(self, response):
        #pagelin=self.next_page
        items=[]


        for i in range (2,22):

            l=response.xpath('//*[@id="car_list_sort"]/div/div/div[4]/table/tbody/tr['+str(i)+']/td[2]/div/a//@href').get()
            items.append(l)
        for i in items:
              self.f_lst.append(i)
              #self.f_lst.append(pagelin)

        df = pd.DataFrame(self.f_lst)
        df.columns = ['link_name']



        lnks = pd.read_csv('page_links.csv')
        # Drop first row using drop()
        lnks.drop(index=lnks.index[0], axis=0, inplace=True)
        lks = lnks['page_links'].values.tolist()

        for i in lks:
           next_page = i
           yield scrapy.Request(next_page,callback=self.parse)

           x = pd.DataFrame(items)
           yield df.to_csv('lk.csv')

process = CrawlerProcess()
process.crawl(JanJapanSpider)

process.start()

