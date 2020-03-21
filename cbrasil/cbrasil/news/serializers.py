from django.contrib.auth.models import User, Group

from rest_framework import serializers

from cbrasil.news.models import News, Events, Sources


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Events
        fields = '__all__'

class SourcesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sources
        fields = '__all__'