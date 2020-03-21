from rest_framework.generics import ListAPIView
from rest_framework import filters

from cbrasil.news.serializers import NewsSerializer, AchievementsSerializer, SourcesSerializer
from cbrasil.news.models import News, Achievements, Sources

class NewsView(ListAPIView):

    queryset = News.objects.all().order_by('-created')
    serializer_class = NewsSerializer

class AchievementsView(ListAPIView):

    queryset = Achievements.objects.all().order_by('-created')
    serializer_class = AchievementsSerializer

class SourcesView(ListAPIView):

    queryset = Sources.objects.all().order_by('-created')
    serializer_class = SourcesSerializer