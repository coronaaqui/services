from django.urls import path

from cbrasil.organizations.views import OrganizationsView, SectorsView


urlpatterns = [
    path('', OrganizationsView.as_view(), name='main_organizations'),
    path('sectors/', SectorsView.as_view(), name='sectors'),
]