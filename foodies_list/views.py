from django.shortcuts import render
# Create your views here.



def foodies_home(request):

  return render(request, 'foodies_list/foodies_list.html')

def get_post(request):

  return render(request, 'foodies_list/parameter.html')




# def search(request):
#         if request.method == 'GET':
#                 searched = request.GET['searched']        
#                 recipes = Recipe.objects.filter(name__contains=searched)
#                 return render(request, 'searched.html', {'searched': searched, 'recipes': recipes})
#         else:
#                 return render(request, 'searched.html', {})