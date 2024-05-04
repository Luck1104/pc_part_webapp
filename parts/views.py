from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
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

class BuildsView(LoginRequiredMixin, generic.ListView):
    model = Build
    template_name = 'builds'
    paginate_by = 5

    def get_queryset(self):
        return (
            Build.objects.filter(builder=self.request.user)
        )
    
class BuildCreate(CreateView):
    model = Build
    fields = ['cpu', 'gpu', 'storage', 'ram']

class BuildUpdate(UpdateView):
    model = Build
    fields = ['cpu', 'gpu', 'storage', 'ram']

class BuildDelete(DeleteView):
    model = Build
    success_url = reverse_lazy('builds')

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("build-delete", kwargs={"pk": self.object.pk})
            )