from django.shortcuts import render, redirect
from .models import *
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

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

def login_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(request, 'cep/login.html')

