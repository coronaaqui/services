from django.contrib import admin

from cbrasil.news.models import News, Sources, Achievements

admin.site.register(News)
admin.site.register(Sources)
admin.site.register(Achievements)
