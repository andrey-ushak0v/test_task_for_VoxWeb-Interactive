import requests
from bs4 import BeautifulSoup
import csv


HOST = 'https://market.yandex.ru/partners'
URL = 'https://market.yandex.ru/partners/news'

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='news-list__item')
    news = []
    print(items)

    for item in items:
        news.append(
            {
                'title': item.find('div', class_='news-list__item__header').get_text(),
                'link': item.find('div', class_='news-list__item-header').find('a').get('href'),
                
            }
        )
        return news
    
html = get_html(URL)
get_content(html.text)