
from unicodedata import name
from . import views
from django.urls import path,include


urlpatterns=[
    path('',views.homepage,name="home"),
    
    path('gproduct',views.gproduct,name='gproduct'),
    
]