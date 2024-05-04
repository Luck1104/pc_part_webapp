from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.CPUListView.as_view(), name='home'),
    path('cpu/<int:pk>', views.CPUDetailView.as_view(), name='cpu-detail'),
    path('gpu/<int:pk>', views.GPUDetailView.as_view(), name='gpu-detail'),
    path('storage/<int:pk>', views.StorageDetailView.as_view(), name='storage-detail'),
    path('ram/<int:pk>', views.RAMDetailView.as_view(), name='ram-detail'),
]