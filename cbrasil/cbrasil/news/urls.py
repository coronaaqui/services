from django.urls import path

from cbrasil.news.views import NewsView, AchievementsView, SourcesView


urlpatterns = [
    path('', NewsView.as_view(), name='main_news'),
    path('achievements/', AchievementsView.as_view(), name='achievements'),
    path('sources/', SourcesView.as_view(), name='sources'),
]