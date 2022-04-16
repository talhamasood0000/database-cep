from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    object=Members.objects.all()
    
    context={'hello':object}

    return render(request, 'cep/home.html',context)


