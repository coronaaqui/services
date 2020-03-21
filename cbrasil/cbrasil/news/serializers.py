from django.contrib.auth.models import User, Group

from rest_framework import serializers

from cbrasil.news.models import News, Achievements


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = '__all__'

class AchievementsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Achievements
        fields = '__all__'