from bs4 import BeautifulSoup


def get_values_from_html(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        values = soup.find_all(class_='mk-chart__percent')
        return values[0].contents[0], values[1].contents[0], values[2].contents[0]

    except:
        print("Parsing Error")
        return ()


