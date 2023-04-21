from django.shortcuts import render
# blog에서 models의 Post 호출
from diners.models import Post

# Create your views here.
def landing(request):
  # 가장 최근 3개(pk값의 역순) 포스트를 따오기
  recent_posts = Post.objects.order_by('-pk')[:3]
  return render(
    request, 
    'single_pages/landing.html',
    {
      'recent_posts': recent_posts,
    }  
  )

def about_me(request):
  return render(request, 'single_pages/about_me.html')

def portfolio(request):
  return render(request, 'single_pages/portfolio.html')

def toy_pjts(request):
  return render(request, 'single_pages/toy_pjts.html')