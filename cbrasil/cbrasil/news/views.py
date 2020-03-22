from rest_framework.generics import ListAPIView
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from cbrasil.news.serializers import NewsSerializer, SourcesSerializer
from cbrasil.organizations.serializers import EventsSerializer
from cbrasil.news.models import News, Events, Sources

class NewsView(ListAPIView):

    queryset = News.objects.all().order_by('-created')
    serializer_class = NewsSerializer

class EventsView(ListAPIView):

    queryset = Events.objects.all().order_by('-created')
    serializer_class = EventsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['region__initial', 'sector', 'city']

class SourcesView(ListAPIView):

    queryset = Sources.objects.all().order_by('-created')
    serializer_class = SourcesSerializer