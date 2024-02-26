from django.urls import path,include
from .views import *

urlpatterns = [
    path('', PageHomeViews.as_view(), name = 'page')
]
