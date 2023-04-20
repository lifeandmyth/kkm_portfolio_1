from django.shortcuts import render

# Create your views here.

def dashboard(request):
  word = "DASHBOARD"
  return render(request, 'dashboard/chart.html', {"word":word})
