from django.shortcuts import render
from food_costs.models import Eggs, Flour, Sugar, Pepper, SaltedMackerel, SaltedShrimp, Anchovy, Squid, Rice, ChapRice, WhiteBeans, RedBeans
from food_costs.models import FlourFood



# Create your views here.



def foodies_home(request):

    # foodies_op = request.GET.get('foodies')

    return render(request, 'foodies_list/foodies_list.html')

def get_post(request):

    return render(request, 'foodies_list/parameter.html')


    

# 남은건 Eggs가 아닌 특정 클래스(request 받은)의 데이터를 호출하도록 설정시킨다.
def dashboard(request):

    data = Eggs.objects.all()
    name = Eggs.name
    with open('./datas/txt/1eggs.txt', encoding="UTF8") as f:
        contents = f.read().splitlines()
    image_url = '/static/foodies_list/images/eggs_640.jpg'
    context = {
        'dataset' : data,
        'name' : name,
        'image_url' : image_url,
        'contents' : contents,
    }
    return render(request, 'foodies_list/dashboard.html', context)
    # 'date' : date
    # 'foodies_text' : foodies_text,

def foodiesinfo_index(request):
    #   # 드롭다운 항목을 바꾸면 대시보드도 이에 맞춰 바뀜
    foodies_txt = request.GET.get('foodies')
    print(foodies_txt)
    if foodies_txt == "01":
        data = Eggs.objects.all()
        name = Eggs.name
        image_url = '/static/foodies_list/images/eggs_640.jpg'
        with open('./datas/txt/1eggs.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
        
    elif foodies_txt == "02":
        data = Flour.objects.all()
        name = Flour.name
        image_url = '/static/dashboard/images/flour_640.jpg'
        with open('./datas/txt/2flour.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
        
    elif foodies_txt == "03":
        data = Sugar.objects.all()
        name = Sugar.name
        image_url = '/static/foodies_list/images/sugar_640.jpg'
        with open('./datas/txt/3sugar.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "04":
        data = Pepper.objects.all()
        name = Pepper.name
        image_url = '/static/foodies_list/images/pepper_640.jpg'
        with open('./datas/txt/4dried_pepper.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "05":
        data = SaltedMackerel.objects.all()
        name = SaltedMackerel.name
        image_url = '/static/foodies_list/images/mackerel_640.jpg'
        with open('./datas/txt/5salted_mackerel.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "06":
        data = SaltedShrimp.objects.all()
        name = SaltedShrimp.name
        image_url = '/static/foodies_list/images/shrimp_640.jpg'
        with open('./datas/txt/6salted_shrimp.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "07":
        data = Anchovy.objects.all()
        name = Anchovy.name
        image_url = '/static/foodies_list/images/anchovy_640.jpg'
        with open('./datas/txt/7dried_anchovy.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "08":
        data = Squid.objects.all()
        name = Squid.name
        image_url = '/static/foodies_list/images/squid_640.jpg'
        with open('./datas/txt/8water_squid.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "09":
        data = Rice.objects.all()
        name = Rice.name
        image_url = '/static/foodies_list/images/rice_640.jpg'
        with open('./datas/txt/9rice.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "10":
        data = ChapRice.objects.all()
        name = ChapRice.name
        image_url = '/static/foodies_list/images/chap_rice_640.jpg'
        with open('./datas/txt/10chap_rice.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "11":
        data = WhiteBeans.objects.all()
        name = WhiteBeans.name
        image_url = '/static/foodies_list/images/white_beans_640.jpg'
        with open('./datas/txt/11white_beans.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    elif foodies_txt == "12":
        data = RedBeans.objects.all()
        name = RedBeans.name
        image_url = '/static/foodies_list/images/red_beans_640.jpg'
        with open('./datas/txt/12red_beans.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
    

    else:
        data = Eggs.objects.all()
        name = Eggs.name
        image_url = '/static/foodies_list/images/eggs_640.jpg'
        with open('./datas/txt/1eggs.txt', encoding="UTF8") as f:
            contents = f.read().splitlines()
        
    data2 = FlourFood.objects.all()
    name2 = FlourFood.name
    
        

    context = {
        'dataset' : data,
        'name' : name,
        'contents' : contents,
        'image_url' : image_url,
        'dataset2' : data2,
        'name2' : name2,
    }
    return render(request, 'foodies_list/dashboard.html', context)
    

# def search(request):
#         if request.method == 'GET':
#                 searched = request.GET['searched']        
#                 recipes = Recipe.objects.filter(name__contains=searched)
#                 return render(request, 'searched.html', {'searched': searched, 'recipes': recipes})
#         else:
#                 return render(request, 'searched.html', {})