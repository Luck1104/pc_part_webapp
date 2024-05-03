from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.

def index(request):
    context = {

    }
    return render(request, 'index.html', context=context)

class CPUListView(generic.ListView):
    model = CPU
