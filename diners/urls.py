from django.urls import path
from . import views

urlpatterns = [
    
  # path('', views.index),
  # path('<int:pk>/', views.detail_page),
  # CBV로 바꾸기:
  path('', views.PostList.as_view()),
  path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
  # /diners/category/{self.slug}
  # /diners/category/파이썬
  path('category/<str:slug>/', views.catagory_page, name='category_filter'),
  path('tag/<str:slug>/', views.tag_page, name='tag_filter'),
  path('create_post/', views.PostCreate.as_view(), name='post_create'),
  path('search/<str:q>/', views.PostSearch.as_view(), name='post_search'),
  # /diners/update_post/포스트의 pk/로 접근할 때 diners/views.py의 PostUpdate를 사용
  path('update_post/<int:pk>/', views.PostUpdate.as_view()),
  # new_comment 경로를 추가하기(FBV 스타일)
  path('<int:pk>/new_comment/', views.new_comment),
  # 댓글 수정 페이지의 경로(CBV)
  path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
  # 댓글 삭제 페이지의 경로(FBV)
  path('delete_comment/<int:pk>/', views.delete_comment),
  
]