from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home),
    path('gallery/', gallery),
    re_path(r'^archive/(?P<year>[0-9]{4})', archive),   #Using re_path to seek info by the years
    path('about/', about),
]