from django.contrib import admin

from cbrasil.organizations.models import Sectors, Organizations

admin.site.register(Sectors)
admin.site.register(Organizations)