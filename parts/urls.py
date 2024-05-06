from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('home/', views.index, name='index'),
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('cpu/', views.CPUListView.as_view(), name='cpu-list'),
    path('gpu/', views.GPUListView.as_view(), name='gpu-list'),
    path('storage/', views.StorageListView.as_view(), name='storage-list'),
    path('ram/', views.RAMListView.as_view(), name='ram-list'),
    path('cpu/<int:pk>', views.CPUDetailView.as_view(), name='cpu-detail'),
    path('gpu/<int:pk>', views.GPUDetailView.as_view(), name='gpu-detail'),
    path('storage/<int:pk>', views.StorageDetailView.as_view(), name='storage-detail'),
    path('ram/<int:pk>', views.RAMDetailView.as_view(), name='ram-detail'),
    path('builds/', views.BuildsView.as_view(), name='builds'),
    path('builds/create/', views.BuildCreate.as_view(), name='build-create'),
    path('builds/<int:pk>/update/', views.BuildUpdate.as_view(), name='build-update'),
    path('builds/<int:pk>/delete/', views.BuildDelete.as_view(), name='build-delete'),
]