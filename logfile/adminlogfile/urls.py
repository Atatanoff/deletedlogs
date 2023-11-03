from django.urls import path
from adminlogfile import views
 
urlpatterns = [
    path('', views.index),
]