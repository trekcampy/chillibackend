from django.urls import path

from . import views

urlpatterns = [
    path('', views.chillilist, name='chillilist'),
]
