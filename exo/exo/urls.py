from django.urls import path
from exo.exo import views

urlpatterns = [
    path('trackData/', views.trackData_list),
    path('trackData/<int:pk>/', views.trackData_detail),
    path('getStops/<int:idTracker>/', views.getStops_list),
    path('iterationMode/<int:idTracker>/', views.iterationMode),
]