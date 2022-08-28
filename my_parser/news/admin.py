from django.contrib import admin



from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'description', 'tag',)
    fields = ('title', 'link', 'description', 'tag',)
    search_fields = ('title', 'link', 'description', 'tag',)

admin.site.register(News, NewsAdmin)