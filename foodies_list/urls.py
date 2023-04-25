from django.urls import path
from . import views
# from .views import search

urlpatterns = [
  path('', views.foodies_home),
  path('dashboard', views.foodiesinfo_index, name='foodiesinfo_index'),
  # path('search/', views.search, name='search'),
  path('parameter/', views.get_post),
]