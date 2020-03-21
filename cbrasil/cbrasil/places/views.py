from rest_framework.generics import ListAPIView
from rest_framework import filters

from cbrasil.places.serializers import RegionsSerializer, CitiesSerializer
from cbrasil.places.models import Regions, Cities

class RegionsView(ListAPIView):

    queryset = Regions.objects.all().order_by('-created')
    serializer_class = RegionsSerializer

class CitiesView(ListAPIView):

    queryset = Cities.objects.all().order_by('-created')
    serializer_class = CitiesSerializer
