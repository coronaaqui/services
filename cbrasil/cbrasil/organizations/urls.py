from django.urls import path

from cbrasil.organizations.views import OrganizationsView, SectorsView, SectorsEventsView, SectorsEventsRegionsView


urlpatterns = [
    path('', OrganizationsView.as_view(), name='main_organizations'),
    path('sectors/', SectorsView.as_view(), name='sectors'),
    path('sectors/events/', SectorsEventsView.as_view(), name='sectors_events'),
    path('sectors/events/regions/', SectorsEventsRegionsView.as_view(), name='sectors_events_regions'),
]