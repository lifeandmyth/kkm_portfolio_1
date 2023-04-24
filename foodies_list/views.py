from django.shortcuts import render

# Create your views here.


def foodies_home(request):
  return render(request, 'foodies_list/foodies_list.html')