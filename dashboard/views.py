from django.shortcuts import render
# from .models import EggsD
from .models import EggsD

# Create your views here.

def dashboard(request):
  data = EggsD.objects.all()
  name = EggsD.name
  context = {
    'dataset' : data,
    'name' : name
  }
  return render(request, 'dashboard/dashboard.html', context)

  
