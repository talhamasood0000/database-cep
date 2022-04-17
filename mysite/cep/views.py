from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'cep/index.html')

def aboutus(request):
    return render(request, 'cep/about.html')

def contact(request):
    return render(request, 'cep/contact.html')

def teachers(request):
    return render(request, 'cep/teachers.html')

def courses(request):
    return render(request, 'cep/course-grid-2.html')

def blogsingle(request):
    return render(request, 'cep/blog-single.html')

def blog(request):
    return render(request, 'cep/blog.html')