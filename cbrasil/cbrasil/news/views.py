from rest_framework.generics import ListAPIView
from rest_framework import filters

from cbrasil.news.serializers import NewsSerializer, AchievementsSerializer
from cbrasil.news.models import News, Achievements

class NewsView(ListAPIView):

    queryset = News.objects.all().order_by('-created')
    serializer_class = NewsSerializer

class AchievementsView(ListAPIView):

    queryset = Achievements.objects.all().order_by('-created')
    serializer_class = AchievementsSerializer
    search_fields = ['title', 'raw_content']