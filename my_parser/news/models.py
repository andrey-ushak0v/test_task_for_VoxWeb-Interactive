from django.db import models

class News(models.Model):
    title = models.CharField(verbose_name='заголовок', max_length=120)
    link = models.SlugField(verbose_name='ссылка', max_length=600)
    description = models.TextField(verbose_name='описание', max_length=600)
    tag = models.CharField(verbose_name='источник', max_length=40)
