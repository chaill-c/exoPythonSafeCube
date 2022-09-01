from telnetlib import STATUS
from django.contrib.auth.models import User, Group
from exo.exo.models import TrackData
from exo.exo.serializers import TrackDataSerializer, GetStopsSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import pandas as pd, numpy as np
from sklearn.cluster import DBSCAN
import datetime
import json

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
    
@csrf_exempt
def getStops_list(request, idTracker):
    """
    List all stops for tracker X
    """
    try:
        getStops = TrackData.objects.filter(idTracker=idTracker)
    except TrackData.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        stopClusters = pd.DataFrame()
        serializer = GetStopsSerializer(getStops, many=True)
        df = pd.read_json(json.dumps(serializer.data))  
        coords = df[['latitude', 'longitude']].to_numpy()
        kms_per_radian = 6371.0088
        epsilon = 0.05 / kms_per_radian
        db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
        cluster_labels = db.labels_
        num_clusters = len(set(cluster_labels))
        clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
        for i in range(0, num_clusters-1):
            nblines = len(clusters[i])
            if nblines > 1:
                checkDF = pd.DataFrame()
                for j in range(0, nblines-1):
                    checkDF = checkDF.append(df[(df['latitude']==clusters[i][j][0]) & (df['longitude']==clusters[i][j][1])])
                    checkDF.sort_values(by='dateReached', inplace=True)
                    checkDFSize = len(checkDF)
                    date1 = datetime.datetime.strptime(checkDF.iloc[checkDFSize-1]['dateReached'], '%Y-%m-%d %H:%M')
                    date1 = datetime.datetime.timestamp(date1)
                    date2 = datetime.datetime.strptime(checkDF.iloc[0]['dateReached'], '%Y-%m-%d %H:%M')
                    date2 = datetime.datetime.timestamp(date2)
                    tpsMin = (date1-date2)/60
                    if tpsMin > 60:
                        stopClusters = stopClusters.append(checkDF)
        stopClustersLen = len(stopClusters)
        if stopClustersLen > 0:
            return JsonResponse(stopClusters.to_dict(orient="records"), safe=False)
        return HttpResponse(status=201)



@csrf_exempt
def iterationMode(request, idTracker):
    """
    List all stops for tracker X and save new record
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TrackDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status=400)
        try:
            getStops = TrackData.objects.filter(idTracker=idTracker)
        except TrackData.DoesNotExist:
            return HttpResponse(status=404)
    
        stopClusters = pd.DataFrame()
        serializer = GetStopsSerializer(getStops, many=True)
        df = pd.read_json(json.dumps(serializer.data))  
        coords = df[['latitude', 'longitude']].to_numpy()
        kms_per_radian = 6371.0088
        epsilon = 0.05 / kms_per_radian
        db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
        cluster_labels = db.labels_
        num_clusters = len(set(cluster_labels))
        clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
        for i in range(0, num_clusters-1):
            nblines = len(clusters[i])
            if nblines > 1:
                checkDF = pd.DataFrame()
                for j in range(0, nblines-1):
                    checkDF = checkDF.append(df[(df['latitude']==clusters[i][j][0]) & (df['longitude']==clusters[i][j][1])])
                    checkDF.sort_values(by='dateReached', inplace=True)
                    checkDFSize = len(checkDF)
                    date1 = datetime.datetime.strptime(checkDF.iloc[checkDFSize-1]['dateReached'], '%Y-%m-%d %H:%M')
                    date1 = datetime.datetime.timestamp(date1)
                    date2 = datetime.datetime.strptime(checkDF.iloc[0]['dateReached'], '%Y-%m-%d %H:%M')
                    date2 = datetime.datetime.timestamp(date2)
                    tpsMin = (date1-date2)/60
                    if tpsMin > 60:
                        stopClusters = stopClusters.append(checkDF)
        stopClustersLen = len(stopClusters)
        if stopClustersLen > 0:
            print(stopClustersLen)
            return JsonResponse(stopClusters.to_dict(orient="records"), safe=False)
        return HttpResponse(status=201)