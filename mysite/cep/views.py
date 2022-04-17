from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    object=Members.objects.all()
    
    context={'hello':object}

    return render(request, 'cep/index.html',context)


