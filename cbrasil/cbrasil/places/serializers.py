from django.contrib.auth.models import User, Group

from rest_framework import serializers

from cbrasil.places.models import Regions, Cities


class RegionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Regions
        fields = '__all__'

class NestedRegionsSerializer(RegionsSerializer):
    
    def get_field_names(self, declared_fields, info):
        return ['name', 'initial']

class CitiesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cities
        fields = '__all__'

class NestedCitiesSerializer(CitiesSerializer):
    
    def get_field_names(self, declared_fields, info):
        return ['name']
