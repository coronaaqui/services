from django.contrib import admin
from django.db.models import Q

from cbrasil.news.models import News, Sources, Events
from cbrasil.places.models import Regions


class RegionFilter(admin.SimpleListFilter):
    title = 'estado'

    parameter_name = 'region'

    def lookups(self, request, model_admin):
        regions = Regions.objects.all()
        regions_dict = []
        for region in regions:
            regions_dict.append((region.initial, region.name))
        return regions_dict

    def queryset(self, request, queryset):
        value = self.value()
        return queryset.filter(Q(city__region__initial=value) | Q(region__initial=value))

class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'region', 'sector')
    search_fields = ('name',)
    list_filter = ('sector',)
    exclude = ('author',)
    save_as = True

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(News)
admin.site.register(Sources)
admin.site.register(Events, EventsAdmin)
