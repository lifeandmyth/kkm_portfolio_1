from django.urls import path
from . import views

urlpatterns = [
  path('about_me/', views.about_me),
  path('', views.landing),
  path('portfolio/', views.portfolio),
  path('toy_pjts/', views.toy_pjts),
  path('diners_home/', views.diners_home),
]