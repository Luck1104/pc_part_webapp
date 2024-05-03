from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('builds/', views.BuildsView.as_view(), name='builds'),
    path('builds/create/', views.BuildCreate.as_view(), name='build-create'),
    path('builds/<int:pk>/update/', views.BuildUpdate.as_view(), name='build-update'),
    path('builds/<int:pk>/delete/', views.BuildDelete.as_view(), name='build-delete'),
]