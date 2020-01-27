import datetime

import psycopg2
import scrapy
from bs4 import BeautifulSoup
import arrow


month = {
        'january': 1,
        'february': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'august': 8,
        'september': 9,
        'october': 10,
        'november': 11,
        'december': 12
    }

def only_numerics(seq):
    return list(filter(type(seq).isdigit, seq))

class CrossfitInvictus(scrapy.Spider):
    name = 'wodnews_spider'
    start_urls = ['https://www.wodnews.com/category/wod']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.conn = psycopg2.connect("dbname='crossfit' user='postgres' host='localhost'")
        except:
            pass


    def parse(self, response):
        # print('toto',response)
        for title in response.css('.loop-entry-title'):
            yield scrapy.Request(title.css('a::attr(href)').get(), self.collect_wod)


        print(response.css('.page-numbers>li').extract()[1])
        for next_page in response.css('.page-numbers>li'):
            print('nextpage', next_page.css('a::attr(href)').get())
            yield response.follow(next_page, self.parse)

    def collect_wod(self, response):
        #print(response.request.url)
        wod= response.css('.entry.clr>p ::text').extract()
        wod = ' '.join(map(str, wod))



    #     cur = self.conn.cursor()
    #     date_string = response.css('.entry-title *::text').extract()[0][:20].lower()
    #
    #     for key in month:
    #         if date_string.find(key) != -1:
    #             month_to_number = month.get(key)
    #             date_string = date_string.replace(key, '')
    #             break
    #     day_years = date_string.split(',')
    #     day = int(day_years[0])
    #
    #     years = only_numerics(day_years[1])
    #     years = int(''.join(years))
    #     print(years, month, day)
    #     final_date = datetime.datetime(years, month_to_number, day)
    #     list_words = response.css('.entry-content *::text').extract()
    #     text = ' '.join(map(str, list_words))
    #     if 'Recovery Day' in text:
    #         pass
    #     else:
    #         cur.execute("INSERT INTO crossfit_wodscraping(wod, date) VALUES (%s, %s)", [text[6:], final_date])
    #         self.conn.commit()
    #     #     # print('wod', wod.get())
