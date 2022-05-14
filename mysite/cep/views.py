from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import datetime
# Create your views here.

def index(request):
    return render(request, 'cep/index.html')

def aboutus(request):
    return render(request, 'cep/about.html')

def contact(request):
    if request.method == "POST":
        form=ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ContactForm()
    context={'form':form}
    return render(request, 'cep/contact.html',context)

def core_body(request):
    objects=CoreBody.objects.all()
    context={'objects':objects}
    return render(request, 'cep/core_body.html',context)

def teams(request):
    teams=Team.objects.all()
    context={'teams':teams}
    return render(request, 'cep/teams.html',context)

def activities(request):
    activities=Activities.objects.all()
    context={'activities':activities}
    return render(request, 'cep/activities.html',context)

def activity_detail(request,id):
    activity=get_object_or_404(Activities,pk=id)
    context={'activity':activity}
    return render(request, 'cep/activity-detail.html',context)


def register_user(request):
    if request.method == "POST":
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
        l_form=LoginForm(request.POST or None)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            messages.success(request, f'Registration complete! You may log in!')
            return redirect('/')
        if l_form.is_valid():
            username=l_form.cleaned_data.get('username')
            password=l_form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('/')
    else:
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
        l_form = LoginForm(request.POST or None)
    return render(request, 'cep/register.html', {'u_form': u_form, 'p_form': p_form, 'l_form': l_form})

def logout_page(request):
    logout(request)
    return redirect('/register/')


def inventory(request):
    inventorys=Inventory.objects.all()
    context={'inventorys':inventorys}
    return render(request, 'cep/inventory.html',context)

@login_required(login_url='/register/')
def inventory_request(request,slug):
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)

    inventory=get_object_or_404(Inventory,item_id=slug)
    member=Members.objects.get(id=request.user.id)

    inv_req=RequestView.objects.create(item_id=inventory,int_mem_id=member,return_date=next_week)
    inv_req.save()

    reqviews=RequestView.objects.all()
    context={'reqviews':reqviews}
    return render (request, 'cep/inventory-request.html',context)
 