
"""MountainTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MapApp.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('edit/', OpenMap.as_view(), name='edit_map'),
    path('update/',  csrf_exempt(UpdateView.as_view()), name='update_marker'),
    path('',  ListMap.as_view(), name='maps_list'),
    path('create/',  CreateMapView.as_view(), name='create_map'),
]
