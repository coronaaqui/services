from datetime import datetime

from django.db.models import Count, Q

from rest_framework.generics import ListAPIView

from cbrasil.organizations.serializers import SectorsSerializer, OrganizationsSerializer, SectorEventsSerializer
from cbrasil.organizations.models import Sectors, Organizations
from cbrasil.organizations.filters import SectorsAggregationFilters

class SectorsView(ListAPIView):

    serializer_class = SectorsSerializer
    filter_backends = [SectorsAggregationFilters]
    queryset = Sectors.objects.all()

class OrganizationsView(ListAPIView):

    queryset = Organizations.objects.all().order_by('-created')
    serializer_class = OrganizationsSerializer

class SectorsEventsView(ListAPIView):

    queryset = Sectors.objects.all().order_by('-created')
    serializer_class = SectorEventsSerializer
