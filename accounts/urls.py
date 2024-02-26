from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', SignUpViews.as_view(), name = 'signup'),
]
   
