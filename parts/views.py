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
    template_name = 'cpu_list'
    paginate_by = 5

class RAMListView(generic.ListView):
    model = RAM
    template_name = 'ram_list'
    paginate_by = 5

class GPUListView(generic.ListView):
    model = GPU
    template_name = 'gpu_list'
    paginate_by = 5
class StorageListView(generic.ListView):
    model = Storage
    template_name = 'storage_list'
    paginate_by = 5
    
class CPUDetailView(generic.DetailView):
    model = CPU

class GPUDetailView(generic.DetailView):
    model = GPU

class StorageDetailView(generic.DetailView):
    model = Storage

class RAMDetailView(generic.DetailView):
    model = RAM
