from django.shortcuts import render
from food_costs.models import Eggs, Flour, Sugar, Pepper

# Create your views here.

# 남은건 Eggs가 아닌 특정 클래스(request 받은)의 데이터를 호출하도록 설정시킨다.
def dashboard(request):

  data = Eggs.objects.all()
  name = Eggs.name

  context = {
    'dataset' : data,
    'name' : name,
  }
  return render(request, 'dashboard/dashboard2.html', context)
# 'date' : date
# 'foodies_text' : foodies_text,

def foodiesinfo_index(request):
#   # 드롭다운 항목을 바꾸면 대시보드도 이에 맞춰 바뀜
  foodies_txt = request.GET.get('foodies')
  print(foodies_txt)
  if foodies_txt == "01":
    data = Eggs.objects.all()
    name = Eggs.name
  elif foodies_txt == "02":
      data = Flour.objects.all()
      name = Flour.name
  elif foodies_txt == "03":
      data = Sugar.objects.all()
      name = Sugar.name
  elif foodies_txt == "04":
      data = Pepper.objects.all()
      name = Pepper.name
  else:
    data = Eggs.objects.all()
    name = Eggs.name

  context = {
    'dataset' : data,
    'name' : name,
  }
  return render(request, 'dashboard/dashboard2.html', context)
  