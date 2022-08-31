from django.contrib.auth.models import User, Group
from rest_framework import serializers
from exo.exo.models import TrackData, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TrackDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackData
        fields = ['id', 'idTracker', 'dataInfo', 'radius', 'is_done', 'latitude', 'longitude', 'dateReached']

# class TrackDataSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     idTracker = serializers.IntegerField()
#     dataInfo = serializers.CharField(style={'base_template': 'textarea.html'})
#     radius = serializers.IntegerField()
#     is_done = serializers.BooleanField()
#     latitude = serializers.FloatField()
#     longitude = serializers.FloatField()
#     dateReached = serializers.DateTimeField()    

#     def create(self, validated_data):
#         """
#         Create and return a new `TrackData` instance, given the validated data.
#         """
#         return TrackData.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `TrackData` instance, given the validated data.
#         """
#         instance.idTracker = validated_data.get('idTracker', instance.idTracker)
#         instance.dataInfo = validated_data.get('dataInfo', instance.data)
#         instance.radius = validated_data.get('radius', instance.radius)
#         instance.is_done = validated_data.get('is_done', instance.is_done)
#         instance.latitude = validated_data.get('latitude', instance.latitude)
#         instance.longitude = validated_data.get('longitude', instance.longitude)
#         instance.dateReached = validated_data.get('dateReached', instance.date_reached)
        
#         instance.save()
#         return instance