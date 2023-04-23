from django.shortcuts import render
from food_costs.models import Eggs, Flour, Sugar, Pepper, SaltedMackerel, SaltedShrimp, Anchovy, Squid, Rice, ChapRice, WhiteBeans, RedBeans

# Create your views here.

# 남은건 Eggs가 아닌 특정 클래스(request 받은)의 데이터를 호출하도록 설정시킨다.
def dashboard(request):

    data = Eggs.objects.all()
    name = Eggs.name
    with open('./datas/txt/1eggs.txt', encoding="UTF8") as f:
        contents = f.read().splitlines()
    
    context = {
        'dataset' : data,
        'name' : name,
        'contents' : contents,
    }
    return render(request, 'dashboard/dashboard.html', context)
    # 'date' : date
    # 'foodies_text' : foodies_text,

def foodiesinfo_index(request):
    #   # 드롭다운 항목을 바꾸면 대시보드도 이에 맞춰 바뀜
    foodies_txt = request.GET.get('foodies')
    print(foodies_txt)
    if foodies_txt == "01":
        data = Eggs.objects.all()
        name = Eggs.name
        with open('./datas/txt/1eggs.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
        
    elif foodies_txt == "02":
        data = Flour.objects.all()
        name = Flour.name
        with open('./datas/txt/2flour.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
        
    elif foodies_txt == "03":
        data = Sugar.objects.all()
        name = Sugar.name
        with open('./datas/txt/3sugar.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "04":
        data = Pepper.objects.all()
        name = Pepper.name
        with open('./datas/txt/4dried_pepper.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "05":
        data = SaltedMackerel.objects.all()
        name = SaltedMackerel.name
        with open('./datas/txt/5salted_mackerel.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "06":
        data = SaltedShrimp.objects.all()
        name = SaltedShrimp.name
        with open('./datas/txt/6salted_shrimp.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "07":
        data = Anchovy.objects.all()
        name = Anchovy.name
        with open('./datas/txt/7dried_anchovy.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "08":
        data = Squid.objects.all()
        name = Squid.name
        with open('./datas/txt/8water_squid.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "09":
        data = Rice.objects.all()
        name = Rice.name
        with open('./datas/txt/9rice.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "10":
        data = ChapRice.objects.all()
        name = ChapRice.name
        with open('./datas/txt/10chap_rice.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "11":
        data = WhiteBeans.objects.all()
        name = WhiteBeans.name
        with open('./datas/txt/11white_beans.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "12":
        data = RedBeans.objects.all()
        name = RedBeans.name
        with open('./datas/txt/12red_beans.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    

    else:
        data = Eggs.objects.all()
        name = Eggs.name
        with open('./datas/txt/1eggs.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
        


    context = {
        'dataset' : data,
        'name' : name,
        'contents' : contents,
    }
    return render(request, 'dashboard/dashboard.html', context)
    