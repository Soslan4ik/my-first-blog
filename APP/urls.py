from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_insert/', views.index, name='index'),
]