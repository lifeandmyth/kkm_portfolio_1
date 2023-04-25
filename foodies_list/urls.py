from django.urls import path
from . import views
# from .views import search

urlpatterns = [
  path('', views.foodies_home),
  path('dashboard/', views.foodiesinfo_index, name='foodiesinfo_index'),
  # path('dashboard/?foodies==<str:q>/', views.get_dashboard_url, name='get_dashboard_url'),
  # path('search/', views.search, name='search'),
]