import datetime

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse
from magie_o_meter.db_config import inster_date_to_database


""" This crawler didn't work at the moment, because there are new values... """


class MagieSpider(scrapy.Spider):
    name = "magieValue"
    # date = datetime.date.today().strftime("%d-%m-%Y")

    def __init__(self, **kw):
        super(MagieSpider, self).__init__(**kw)
        url = kw.get('url') or kw.get('domain')
        self.date = kw.get('date')
        self.url = url
        self.link_extractor = LinkExtractor()

    def start_requests(self):
        return[Request(self.url, callback=self.parse, dont_filter=True)]

    def get_values(self):
        return (self.magie_o_meter_value, self.impuls_value, self.bw_value)

    def parse(self, response):
        self.magie_o_meter_value = response.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/article/div[3]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/span/text()').get()
        self.impuls_value = response.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/article/div[3]/div[2]/div/div[4]/div[3]/div/div/div/div[1]/span/text()').get()
        self.bw_value = response.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/article/div[3]/div[2]/div/div[6]/div[3]/div/div/div/div[1]/span/text()').get()
        inster_date_to_database(self.date, self.magie_o_meter_value, self.impuls_value, self.bw_value)
        print(self.magie_o_meter_value, self.impuls_value, self.bw_value)

        """print(f"\n\n\n\n\n\n\nIch bin eindeutiger Text : {magie_o_meter_value}, {impuls_value} {bw_value}")"""




