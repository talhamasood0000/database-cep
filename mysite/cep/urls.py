from django import views
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('aboutus/',views.aboutus,name='aboutus'),
   path('contact/',views.contact,name='contact'),
   path('teachers/',views.teachers,name='teachers'),
   path('courses/',views.courses,name='courses'),
   path('blogsingle/',views.blogsingle,name='blogsingle'),
   path('blog/',views.blog,name='blog'),
] 