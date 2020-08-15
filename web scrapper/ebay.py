import csv
import requests
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)
    # print(response.ok)

    if not response.ok:
        print('server responded: ', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_detail_data(soup):
    # item
    # detail
    # item sold
    try:
        external_span = soup.find('h1', id='itemTitle')
        unwanted = external_span.find('span', class_='g-hdn')
        unwanted.extract()
        title = external_span.text.strip().replace('🎁', '')
    except:
        title = None

    try:
        p = soup.find('span', id='prcIsum').text.strip()
        currency, price = p.split(' ')
    except:
        p = soup.find('span', id='mm-saleDscPrc').text.strip()
        p = p.split(' ')
        currency = p[0]
        price = p[1]
        price = price.split('$')[1]

    try:
        unit_sold = soup.find(
            'a', class_='vi-txt-underline').text.split(' ')[0]
    except:
        unit_sold = None

    data = {
        'title': title,
        'price': price,
        'currency': currency,
        'unit_sold': unit_sold
    }

    return data


# to access all links to each item
def get_index_data(soup):
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []

    url = [item.get('href') for item in links]

    return url


def write_csv(data, url):
    with open('output.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([data['title'], data['price'],
                         data['currency'], data['unit_sold'], url])


def main():
    url = 'https://www.ebay.com.my/sch/i.html?_nkw=mens+watches&-pgn=2'

    products = get_index_data(get_page(url))

    for link in products:
        data = get_detail_data(get_page(link))
        print(data)
        write_csv(data, link)


if __name__ == '__main__':
    main()
