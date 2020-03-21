from django.contrib import admin

# Register your models here.
from cbrasil.places.models import Regions, Cities

admin.site.register(Regions)
admin.site.register(Cities)