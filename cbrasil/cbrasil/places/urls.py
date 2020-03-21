from django.urls import path

from cbrasil.places.views import RegionsView, CitiesView


urlpatterns = [
    path('cities/', CitiesView.as_view(), name='cities'),
    path('regions/', RegionsView.as_view(), name='regions'),
]