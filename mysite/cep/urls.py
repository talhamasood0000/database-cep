from django import views
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.index,name='index'),
   path('aboutus/',views.aboutus,name='aboutus'),
   path('contact/',views.contact,name='contact'),
   path('core_body/',views.core_body,name='core_body'),
   path('courses/',views.courses,name='courses'),
   path('blogsingle/',views.blogsingle,name='blogsingle'),
   path('activities/',views.activities,name='activities'),
   path('login/',views.login_user,name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



