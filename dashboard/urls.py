from django.urls import path
from .views import dashboard
from . import views

app_name = 'dashboard'
urlpatterns = [
    
    path('', views.foodiesinfo_index, name='foodiesinfo_index'),
    path('', dashboard, name='dashboard'),
]