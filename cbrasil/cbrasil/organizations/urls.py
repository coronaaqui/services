from django.urls import path

from cbrasil.organizations.views import OrganizationsView, SectorsView, SectorsEventsView


urlpatterns = [
    path('', OrganizationsView.as_view(), name='main_organizations'),
    path('sectors/', SectorsView.as_view(), name='sectors'),
    path('sectors/events/', SectorsEventsView.as_view(), name='sectors'),
]