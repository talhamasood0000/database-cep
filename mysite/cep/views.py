from django.shortcuts import get_object_or_404, render, redirect
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

def activity_detail(request,id):
    activity=get_object_or_404(Activities,pk=id)
    context={'activity':activity}
    return render(request, 'cep/activity-detail.html',context)

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

 