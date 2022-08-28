import json

from django.core.management.base import BaseCommand
from news.models import News


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('news.json', 'rb') as f:
            data = json.load(f)
            for i in data:
                news = News()
                news.title = i['title']
                news.link = i['link']
                news.description = i['description']
                news.tag = i['tag']
                news.save()
                print(i['title'], i['link'], i['description'], i['tag'])
