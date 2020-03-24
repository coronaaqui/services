from django.urls import path

from cbrasil.news.views import NewsView, EventsView, SourcesView, EventsRegionsView


urlpatterns = [
    path('', NewsView.as_view(), name='main_news'),
    path('events/', EventsView.as_view(), name='events'),
    path('events/regions', EventsRegionsView.as_view(), name='events_regions'),
    path('sources/', SourcesView.as_view(), name='sources'),
]