from rest_framework.generics import ListAPIView
from rest_framework import filters

from cbrasil.organizations.serializers import SectorsSerializer, OrganizationsSerializer, SectorEventsSerializer
from cbrasil.organizations.models import Sectors, Organizations

class SectorsView(ListAPIView):

    queryset = Sectors.objects.all().order_by('-created')
    serializer_class = SectorsSerializer

class OrganizationsView(ListAPIView):

    queryset = Organizations.objects.all().order_by('-created')
    serializer_class = OrganizationsSerializer

class SectorsEventsView(ListAPIView):

    queryset = Sectors.objects.all().order_by('-created')
    serializer_class = SectorEventsSerializer
