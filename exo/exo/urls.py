from django.urls import path
from exo.exo import views

urlpatterns = [
    path('trackData/', views.trackData_list),
    path('trackData/<int:pk>/', views.trackData_detail),
]