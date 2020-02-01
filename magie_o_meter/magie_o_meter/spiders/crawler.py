import scrapy

from magie_o_meter.db_config import inster_date_to_database

""" This crawler didn't work at the moment, because there are new values... """

class QuotesSpider(scrapy.Spider):
    name = "magieValue"
    # date = datetime.date.today().strftime("%d-%m-%Y")

    start_urls = [

    ]

    for i in range(1,13):
        for j in range(1,32):
            for k in range(2018,2020):
                if i < 10:
                    if j < 10:
                        date = f"0{j}-0{i}-{k}"
                        start_urls.append(f'https://tagesenergie.org/energie-des-tages/tagesenergie-am-{date}/')
                    else:
                        date = f"{j}-0{i}-{k}"
                        start_urls.append(f'https://tagesenergie.org/energie-des-tages/tagesenergie-am-{date}/')
                else:
                    if j < 10:
                        date = f"0{j}-{i}-{k}"
                        start_urls.append(f'https://tagesenergie.org/energie-des-tages/tagesenergie-am-{date}/')
                    else:
                        date = f"{j}-{i}-{k}"
                        start_urls.append(f'https://tagesenergie.org/energie-des-tages/tagesenergie-am-{date}/')



    print(start_urls)


    def parse(self, response):
        magie_o_meter_value = response.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/article/div[3]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/span/text()').get()
        impuls_value = response.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/article/div[3]/div[2]/div/div[4]/div[3]/div/div/div/div[1]/span/text()').get()
        bw_value = response.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/article/div[3]/div[2]/div/div[6]/div[3]/div/div/div/div[1]/span/text()').get()
        print(f"\n\n\n\n\n\n\nIch bin eindeutiger Text : {magie_o_meter_value}, {impuls_value} {bw_value}")
        #inster_date_to_database(self.date, magie_o_meter_value, impuls_value, bw_value)




