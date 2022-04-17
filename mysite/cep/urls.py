from django import views
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('aboutus/',views.aboutus,name='aboutus'),
] 