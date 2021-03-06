
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
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path, include
from FoodApp.views import *

urlpatterns = [path('edit/', login_required(EditCalculator.as_view()), name='update_calculator'),
               path('add-item/', AddItemCalculator.as_view(), name='add_food'),
               path('delete-item/', DeleteItemCalculator.as_view(), name='delete_food'),
               path('', login_required(ListCalculators.as_view()), name='calculators_list'),
               path('create/', CreateCalculatorView.as_view(), name='create_calculator'),
               path('add-day/', AddDayCalculator.as_view(), name='add_day'),
               path('delete-day/', DeleteDayCalculator.as_view(), name='delete_day'),

]
