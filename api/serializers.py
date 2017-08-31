from rest_framework import serializers
from client.models import *

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['drink']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location']

class DrinkSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkSurvey
        fields = ['research_person','research_area','drink']