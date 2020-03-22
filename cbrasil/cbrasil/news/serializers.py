from django.contrib.auth.models import User, Group

from rest_framework import serializers

from cbrasil.news.models import News, Events, Sources
from cbrasil.places.serializers import NestedRegionsSerializer, NestedCitiesSerializer

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NestedNewsSerializer(NewsSerializer):

    def to_representation(self, instance):
        fields = super().to_representation(instance)
        fields['source'] = instance.source.name
        return fields

    def get_field_names(self, declared_fields, info):
        return ['title', 'source', 'text', 'link']


class SourcesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sources
        fields = '__all__'