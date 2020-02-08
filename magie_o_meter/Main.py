import time
import urllib.request
from magie_o_meter.XMLParser import get_values_from_html
from magie_o_meter.db_config import inster_date_to_database
from scrapy.crawler import CrawlerProcess


def main():
    start_urls = []
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



    for url in start_urls:
        date = ''
        for i in range(59,69):
            date = date + url[i]
        time.sleep(5)
        try:
            html = request_data(url)
        except:
            print("Error scraping")
            html = ""

        # html = open('website.html', "r")
        values = get_values_from_html(html)

        try:
            inster_date_to_database(date, values[0], values[1], values[2])
        except:
            print("Insert Error")
            inster_date_to_database(date, 0,0,0)


def request_data(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read()
    # print(html)
    return html

if __name__ == "__main__":
    main()