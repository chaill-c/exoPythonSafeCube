from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from exo.exo.models import TrackData
from exo.exo.serializers import UserSerializer, GroupSerializer, TrackDataSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def trackData_list(request):
    """
    List all trackDatas, or create a new trackData.
    """
    if request.method == 'GET':
        trackData = TrackData.objects.all()
        serializer = TrackDataSerializer(trackData, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TrackDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def trackData_detail(request, pk):
    """
    Retrieve, update or delete a trackData.
    """
    try:
        trackData = TrackData.objects.get(pk=pk)
    except TrackData.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TrackDataSerializer(trackData)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TrackDataSerializer(trackData, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        trackData.delete()
        return HttpResponse(status=204)