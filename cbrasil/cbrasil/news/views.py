from rest_framework.generics import ListAPIView
from rest_framework import filters

from cbrasil.news.serializers import NewsSerializer, EventsSerializer, SourcesSerializer
from cbrasil.news.models import News, Events, Sources

class NewsView(ListAPIView):

    queryset = News.objects.all().order_by('-created')
    serializer_class = NewsSerializer

class EventsView(ListAPIView):

    queryset = Events.objects.all().order_by('-created')
    serializer_class = EventsSerializer

class SourcesView(ListAPIView):

    queryset = Sources.objects.all().order_by('-created')
    serializer_class = SourcesSerializer