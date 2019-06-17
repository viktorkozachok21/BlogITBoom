from django.contrib import admin
from .models import Article, News, RunabledNews, ContactMessage, OfferMessage, ComputerLanguage, Song

# Register your models here.
admin.site.register(Article)
admin.site.register(News)
admin.site.register(RunabledNews)
admin.site.register(ContactMessage)
admin.site.register(OfferMessage)
admin.site.register(ComputerLanguage)
admin.site.register(Song)
