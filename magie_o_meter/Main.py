import time
import urllib.request
import urllib.error
import sys
from random import random, randrange

from magie_o_meter.XMLParser import get_values_from_html
from magie_o_meter.db_config import inster_date_to_database
from scrapy.crawler import CrawlerProcess


# TODO After crawling all values, select every 0 value from db and start search again only with this dates
# TODO automate restart after banning: push to git and with restart load and change start values in start_urls


def main():
    start_urls = []
    for k in range(2018, 2020):
        for i in range(1, 13):
            for j in range(1, 32):
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

    start_urls = start_urls[41:]

    # start_urls = ["https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/"]

    for url in start_urls:
        date = ''
        for i in range(59, 69):
            # pass
            date = date + url[i]
        sleep_time = randrange(5, 100)
        time.sleep(sleep_time)
        try:
            html = request_data(url)
        except urllib.error.HTTPError as e:
            if e.code == 403:
                f = open('last_request.txt', 'w')
                f.write(url)
                f.close()
                sys.exit()
            print(e)
            html = ""
        except Exception as e:
            print(f"Error scraping {e}")
            html = ""

        # html = open('website.html', "r")
        values = get_values_from_html(html)

        try:
            inster_date_to_database(date, values[0], values[1], values[2])
        except:
            print("Insert Error")
            inster_date_to_database(date, 0, 0, 0)


def request_data(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read()
    # print(html)
    return html


if __name__ == "__main__":
    main()
