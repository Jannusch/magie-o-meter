import time
import urllib.request
import urllib.error
import sys
from random import random, randrange
import datetime

from XMLParser import get_values_from_html
from db_config import inster_date_to_database


def main():
    date = datetime.datetime.now().date()
    day = date.day
    month = date.month
    year = date.year

    if month < 10:
        month = f'0{month}'

    if day < 10:
        day = f'0{day}'

    url = f'https://tagesenergie.org/energie-des-tages/energie-des-tages-tagesenergie-am-{day}-{month}-{year}/'
    date = f'{year}-{month}-{day}'

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
