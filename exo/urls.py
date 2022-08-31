from django.urls import include, path

urlpatterns = [
    path('', include('exo.exo.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]