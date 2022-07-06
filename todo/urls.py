from django.urls import URLPattern, path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name = 'home'),
    path('add/', views.add, name = 'add'),
    path('show/<str:pk>/', views.show, name = 'show'),
    path('edit/<str:pk>/', views.edit, name = 'edit'),
    path('delete/<str:pk>/', views.delete, name = 'delete'),
]