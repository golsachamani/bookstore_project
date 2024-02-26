from django.urls import path,include
from .views import *

urlpatterns = [
    path('home', PageHomeViews.as_view(), name = 'page')
]
