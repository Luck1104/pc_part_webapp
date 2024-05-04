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

class CPUDetailView(generic.DetailView):
    model = CPU

class GPUDetailView(generic.DetailView):
    model = GPU

class StorageDetailView(generic.DetailView):
    model = Storage

class RAMDetailView(generic.DetailView):
    model = RAM
