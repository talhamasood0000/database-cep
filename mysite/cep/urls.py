from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.index,name='index'),
   path('aboutus/',views.aboutus,name='aboutus'),
   path('contact/',views.contact,name='contact'),
   path('core_body/',views.core_body,name='core_body'),
   path('teams/',views.teams,name='teams'),
   path('activity_detail/<int:id>',views.activity_detail,name='activity_detail'),
   path('activities/',views.activities,name='activities'),
   path('register/',views.register_user,name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



 