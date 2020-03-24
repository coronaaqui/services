from itertools import groupby

from rest_framework.generics import ListAPIView
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, Q, Case, F, CharField, When

from cbrasil.news.serializers import NewsSerializer, SourcesSerializer, BaseEventsSerializer
from cbrasil.organizations.serializers import EventsSerializer
from cbrasil.news.models import News, Events, Sources

from rest_framework.renderers import JSONRenderer

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


class EventsRegionsView(ListAPIView):

    serializer_class = BaseEventsSerializer

    def get_queryset(self):
        qs = Events.objects.annotate(
            regiao=Case(
                When(region=None, then=F('city__region')),
                default=F('region'),
                output_field=CharField(),
        )).values('regiao', 'sector').order_by('sector')
        regions_affecteds = []
        for key, group in groupby(qs, lambda x: x['sector']):
            added = []
            for thing in group:
                if thing['regiao'] not in added:
                    added.append(thing['regiao'])
            regions_affecteds.append({'sector':key, 'regions': len(added)})
        return sorted(regions_affecteds, key=lambda x: x['regions'], reverse=True)