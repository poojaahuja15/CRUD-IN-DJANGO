from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.VehicleList, name='vehiclelist'),
    path('add/', views.VehicleCreateView.as_view(), name='adddata'),
    path('delete/<int:pk>/', views.VehicleDeleteView.as_view(), name='deletedata'),
    path('<int:pk>/', views.VehicleUpdate.as_view(), name='updatedata'),
]
