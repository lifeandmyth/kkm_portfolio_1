from django.shortcuts import render
# from .models import EggsD
from food_costs.models import Eggs

# Create your views here.

def dashboard(request):
  data = Eggs.objects.all()
  name = Eggs.name
  context = {
    'dataset' : data,
    'name' : name
  }
  return render(request, 'dashboard/dashboard.html', context)

  
