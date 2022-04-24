from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'cep/index.html')

def aboutus(request):
    return render(request, 'cep/about.html')

def contact(request):
    return render(request, 'cep/contact.html')

def core_body(request):
    objects=CoreBody.objects.all()
    context={'objects':objects}
    return render(request, 'cep/core_body.html',context)

def courses(request):
    return render(request, 'cep/course-grid-2.html')

def activities(request):
    activities=Activities.objects.all()
    context={'activities':activities}
    return render(request, 'cep/activities.html',context)

def blogsingle(request):
    return render(request, 'cep/blog-single.html')

