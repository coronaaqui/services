from django.urls import path

from cbrasil.news.views import NewsView, AchievementsView


urlpatterns = [
    path('', NewsView.as_view(), name='main_news'),
    path('achievements/', AchievementsView.as_view(), name='achievements'),
]