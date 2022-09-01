from django.contrib.auth.models import User, Group
from rest_framework import serializers
from exo.exo.models import TrackData, LANGUAGE_CHOICES, STYLE_CHOICES

class TrackDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackData
        fields = ['id', 'idTracker', 'dataInfo', 'radius', 'is_done', 'latitude', 'longitude', 'dateReached']

class GetStopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackData
        fields = [ 'id', 'latitude', 'longitude', 'dateReached']