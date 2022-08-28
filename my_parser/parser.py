import json

import requests
from bs4 import BeautifulSoup

CSV = 'news.json'
HOST = 'https://market.yandex.ru'
URL = 'https://market.yandex.ru/partners/news'

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content_yandex(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='news-list__item', limit=10)
    news = []
    for item in items:
        news.append( 
            {
                'title': item.find('div', class_='news-list__item-header').get_text(strip=True),
                'link':HOST + item.find('a', class_='link').get('href'),
                'description': item.find('div', class_='news-list__item-description').find('p').get_text(),
                'tag': 'yandex'
            }
        )
    return news

def save_csv(items, flename):
    items = json.dumps(items)
    items = json.loads(str(items))
    with open(flename, 'w', newline='') as file:
        json.dump(items, file, indent=4, ensure_ascii=False)

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        html = get_html(URL)
        save_csv(get_content_yandex(html.text), CSV)

parser()
