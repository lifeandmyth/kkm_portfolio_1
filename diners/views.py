from django.shortcuts import render, redirect
#포스트 수정 기능의 PostUpdate는 UpdateView를 사용하므로 추가:
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# +Comment 모델을 사용하기 위한 호출
from .models import Post, Category, Tag, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#.forms의 PostForm 내용을 여기에 적용한다:
from .forms import PostForm
# question을 받는 장고 내장 모델 Q. boolean으로 q(검색창에 입력한 값)을 포함하느냐 안하느냐를 따져 결과를 반환한다.
from django.db.models import Q
# 수정할 사용자가 author와 일치하는지 여부를 확인하는 모듈을 제공하는 클래스
from django.core.exceptions import PermissionDenied
# slug 값을 관리자 페이지처럼 생성해주는 함수 호출:
from django.utils.text import slugify
# CommentFrom을 PostDetail에 넘겨주기 위해 import
from .forms import CommentForm
# Post.objects.get(pk=pk)가 불러올 때 해당되는 pk값이 없을 경우 404오류를 발생시키도록 하는 모듈:
from django.shortcuts import get_object_or_404


# def index(request):
#   posts = Post.objects.all().order_by('-pk')
#   # 오름차순이면 pk, 내림차순이면 -pk (즉 최신게시물을 상단에 올리려면 내림차순인 -pk)

#   return render(request, 'diners/index.html',
#     {
#       'posts' : posts,
#     }              
#   )
# def detail_page(request, pk):
#   # post를 정의한다. rendering 처리 이후 이 변수를 해당 html 문서에 적용할 수 있다.
#   post = Post.objects.get(pk=pk)

#   return render(
#     request,
#     'diners/detail_page.html',
#     {
#       'post' : post,
#     }
#   )
# 위 코드들을 CBV로 바꾼다면: ↓


class PostList(ListView):
  # 데이터를 가져올 queryset
  model = Post
  # 해당 기본키primary key값에 해당되는 Post 내 업로드한 게시물 중 가장 최근 것(Post 레코드 중 pk값이 작은 순서)을 표시하기 위해 -pk로 선언.
  ordering = '-pk'
  # paginate_by: 한 페이지 당 보여줄 포스트 갯수. pagination할 거면 이 속성을 정의해야 함.
  paginate_by = 5

  # template_name = 'diners/post_list.html'
  #cf. html이름으로 (클래스 이름('List'는 제외))_list.html이 내부적으로 정의가 되어있다(고로 생략).
  #파일명을 임의로 만들 때는 위와 같이 명시해 줘야 함.

  #get_context_data() 메서드로 category 관련 인자 넘기기
  def get_context_data(self, **kwargs):
    # 일단 PostList의 부모인 ListView의 get_context_data()를 실행해 얻은 값을 context에 대입.
    # 이건 ListView를 상속받을 경우 기본으로 실행되는 선언문이므로 이런 두 가지 이상의 값을 context에 대입시켜야 하는 특수한 상황이 아니면 생략 가능.
    # get_context_data()는 Dict형으로 값을 내보낸다.
    context = super(PostList, self).get_context_data() 
    # context에 추가로 Category.objects.all()를 'catagories'라는 이름의 키에 연결해 담습니다.
    context['categories'] = Category.objects.all()
        
    # Post 테이블에서 category 필드를 선택 안 한 포스트의 갯수
    context['no_category_post_count'] = Post.objects.filter(category=None).count()
    
    return context
  
  
class PostDetail(DetailView):
  model = Post
  # template_name = 'diners/post_detail.html'

  def get_context_data(self, **kwargs):
    context = super(PostDetail, self).get_context_data() 
    # context에 추가로 Category.objects.all()를 'catagories'라는 이름의 키에 연결해 담습니다.
    context['categories'] = Category.objects.all()
    # Post 테이블에서 category 필드를 선택 안 한 포스트의 갯수
    context['no_category_post_count'] = Post.objects.filter(category=None).count()
    
    # comment_form이라는 이름으로 CommentForm을 넘겨주기:
    context['comment_form'] = CommentForm

    return context


def catagory_page(request, slug):
  context = {}

  #미분류 카테고리 처리
  if slug == 'no_category':
    category = '미분류'
    context['post_list'] = Post.objects.filter(category=None)

  else:
    #선택한 슬러그에 해당하는 Category테이블의 레코드
    category = Category.objects.get(slug=slug)
    context['post_list'] = Post.objects.filter(category=category)
  

  context['categories'] = Category.objects.all()
  #Post 테이블에서 category 필드를 선택 안 한 포스트의 갯수.
  context['no_category_post_count'] = Post.objects.filter(category=None).count()
  context['category'] = category

  print(context)
  return render(
    request, 
    'diners/post_list.html',
    context
  )
  # return render(
  #   request, 
  #   'diners/post_list.html',
  #   {
  #     'post_list' : Post.objects.filter(category=category),
  #     'categories' : Category.objects.all(),
  #     'no_category_post_count' : Post.objects.filter(category=None).count(),
  #     'category' : category,
  #   }
  # )

def tag_page(request, slug):
  context = {}

  #미분류 카테고리 처리할게 없다 -> 처리 과정 삭제
  #선택한 슬러그에 해당하는 Tag테이블의 레코드
  tag = Tag.objects.get(slug=slug)
  #context 딕셔너리 내 'post_list' 키에, tag에 post_set.all()를 연결시킨, 즉 태그에 연결된 포스트 전체를 저장시킨다.
  context['post_list'] = tag.post_set.all()
  
  #아래는 side widget을 실행하기 위한 부분.
  #모든 카테고리를 가져옴.
  context['categories'] = Category.objects.all()
  #Post 테이블에서 category 필드를 선택 안 한 포스트의 갯수.
  context['no_category_post_count'] = Post.objects.filter(category=None).count()
  context['tag'] = tag

  
  # dict type으로 구성한 데이터를 html 템플릿으로 랜더링 후, 해당 링크 파일로 response한다.
  return render(
    request, 
    'diners/post_list.html',
    context
  )

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
  model = Post
  # class를 받으므로 form_class 변수를 사용해야 한다:
  form_class = PostForm
  # template_name = 'diners/post_form.html' (하지만 내부적으로 이미 post_form.html로 설정되있기에 생략 가능)
  # fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']
  # 위 fields는 PostForm에서 정의해줬기에 중복 언급할 필요가 없다.

  # 이 페이지에 접근 가능한 사용자를 superuser(최고 관리자) 또는 staff(스태프)로 제한한다.
  def test_func(self):
    return self.request.user.is_superuser or self.request.user.is_staff

  def form_valid(self, form):
    current_user = self.request.user
    # 유저가 인증되었다면:
    if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
      form.instance.author = current_user
      # return super(PostCreate, self).form_valid(form)
      # 여기서 name='tags_str'인 input 요소에 입력된 태그 값을 self.object의 태그 필드에 추가해야하기에, 위 값을 response라는 변수에 임시로 담아둔다.
      response = super(PostCreate, self).form_valid(form)

      # post_form.html은 method="post"로 설정되있으니, 이 폼 안에 name='tags_str'인 input을 추가하여 방문자가 submit할 때 이 값 역시 POST 방식으로 PostCreate까지 전달되있는 상태. => 이 값은 self.request.POST.get('tags_str')로 받을 수 있다.
      tags_str = self.request.POST.get('tags_str')
      # 이 입력값이 빈 칸일 때 예외처리 및 구분자 처리
      if tags_str: 
        # 빈칸(스페이스)은 제거
        tags_str = tags_str.strip()
        # ,를 전부 ;로 바꾸기
        tags_str = tags_str.replace(',', ';')
        # ;를 구분자로 처리하고 tags_list에 담기.
        tags_list = tags_str.split(';')

        # #doit_django#파이썬
        # => ['', 'doit_django', '파이썬']
        # doit_django;파이썬;
        # => ['doit_django', '파이썬', '']
        for t in tags_list:
          # 문자열 앞 뒤 공백 제거
          t = t.strip()
          print(t)
          # 이 값을 name을 갖는 태그가 온다면 가져오고, 없다면 새로 만들기. get_or_create()은 첫 번째 Tag모델의 인스턴스를 가져오고, 두 번째로 이 인스턴스가 새로 생성되었는지를 나타내는 bool 값.
          tag, is_tag_created = Tag.objects.get_or_create(name=t)
          print(f'tag, is_tag_created : {tag}, {is_tag_created}')
          
          # t가 공백일 때는 pass(for문 첫문장으로 이동, 다음 요소로 수행)
          if tag == "": 
            # 요소들 중간에 ' '가 들어갈 수도 있기에 후속으로 따라올 태그들을 고려해 break가 아닌 continue
            # 순서는 위에서 아래로 진행되기에 위아래 조건문을 if_else나 상하관계로 놓지 않아도 continue로 for문 앞으로 돌아가니 이대로도 무방하다.
            continue 
          if is_tag_created:
            # slug 자동생성 함수 slugify. 그리고 allow_unicode로 한글도 적용 가능함.
            tag.slug = slugify(t, allow_unicode=True)
            # 그렇게 slug화한 태그를 tag 변수에 추가한다.
            tag.save()
          # 변수 tag를 tags 필드에 추가한다.
          self.object.tags.add(tag)

      return response

    # 아니라면:
    else:
      return redirect('/diners/')


class PostSearch(PostList):
  paginate_by = None

  def get_queryset(self):
    q = self.kwargs['q'] # urls.py의 'search/<str:q>/'의 q값을 대입함.
    post_list = Post.objects.filter(
      Q(title__contains=q) | Q(tags__name__contains=q)
    ).distinct()
    # distinct는 입력된 값이 중복된 요소가 있을때 그 중 하나만 취급한다는 설정.
    return post_list
  
  def get_context_data(self, **kwargs):
    context = super(PostSearch, self).get_context_data()
    q = self.kwargs['q']
    context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

    return context  


# 포스트 수정 기능
class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  # forms.py의 PostForm에서 field값들을 정의하고 있으므로 아래 문구로 축약:
  # 또한 PostForm을 부름으로서 자동으로 django-summernote 라이브러리의 효과도 적용받는다.
  form_class = PostForm
  

  # template_name을 지정해 원하는 html 파일을 템플릿 파일로 설정 -> post_form.html과 겹치지 않도록 조치:
  template_name = 'diners/post_update_form.html'

  # post_update_form.html에서 필요한 tags_str_default를 여기서 정의
  def get_context_data(self, **kwargs):
    # 템플릿으로 추가 인자를 넘기기 위해 get_context_data() 활용:
    context = super(PostUpdate, self).get_context_data()
    # 해당 게시물에 tags 값이 존재한다면:
    if self.object.tags.exists():
      # 변수를 리스트 형태로 만들기
      tags_str_list = list()
      # 그리고 이 리스트의 값들을 세미콜론으로 결합하여 하나의 문자열로 만들기
      for t in self.object.tags.all():
        # 기존 태그 name들을 하나하나 tags_str_list란 리스트형 변수에 입력
        tags_str_list.append(t.name)
      #그리고 그거의 ;과 결합하여 하나의 문자열로 만들고, 'tags_str_default'에 입력.
      context['tag_str_default'] = ';'.join(tags_str_list)
    #이후 담은 값 리턴
    return context

  def form_valid(self, form):
      # PostCreate의 form_valid()를 그대로 가져왔지만 인증 절차는 제외. 어차피 인증된 글 작성자만 해당 페이지에 들어올 수 있으므로.
      # 또한 이미 작성된 포스트라 author 필드가 채워져있다.

      # 여기서 name='tags_str'인 input 요소에 입력된 태그 값을 self.object의 태그 필드에 추가해야하기에, 위 값을 response라는 변수에 임시로 담아둔다.
      response = super(PostUpdate, self).form_valid(form)

      # self.object로 가져온 포스트의 태그를 모두 비워두고, tags_str로 다시 채우도록 한다.
      self.object.tags.clear()

      # post_form.html은 method="post"로 설정되있으니, 이 폼 안에 name='tags_str'인 input을 추가하여 방문자가 submit할 때 이 값 역시 POST 방식으로 PostCreate까지 전달되있는 상태. => 이 값은 self.request.POST.get('tags_str')로 받을 수 있다.
      tags_str = self.request.POST.get('tags_str')
      # 이 입력값이 빈 칸일 때 예외처리 및 구분자 처리
      if tags_str: 
        # 빈칸(스페이스)은 제거
        tags_str = tags_str.strip()
        # ,를 전부 ;로 바꾸기
        tags_str = tags_str.replace(',', ';')
        # ;를 구분자로 처리하고 tags_list에 담기.
        tags_list = tags_str.split(';')

        for t in tags_list:
          # 문자열 앞 뒤 공백 제거
          t = t.strip()
          # 이 값을 name을 갖는 태그가 온다면 가져오고, 없다면 새로 만들기. get_or_create()은 첫 번째 Tag모델의 인스턴스를 가져오고, 두 번째로 이 인스턴스가 새로 생성되었는지를 나타내는 bool 값.
          print(t)
          tag, is_tag_created = Tag.objects.get_or_create(name=t)
          print(tag, is_tag_created)
          if is_tag_created:
            # slug 자동생성 함수 slugify. 그리고 allow_unicode로 한글도 적용 가능함.
            tag.slug = slugify(t, allow_unicode=True)
            # 그렇게 slug화한 태그를 tag 변수에 추가한다.
            tag.save()
          # 변수 tag를 tags 필드에 추가한다.
          self.object.tags.add(tag)

      return response


  # author 필드가 현 사용자(방문자)와 동일한 경우에만 dispatch()가 동작하도록 조건문:
  def dispatch(self, request, *args, **kwargs ):
    # 1.사용자 => 로그인한 대상 & 수정 요청한 대상 
    # 2.그 대상이 author와 일치(==)
    if request.user.is_authenticated and request.user == self.get_object().author:
      # self.get_object()는 Post.objects.get(pk=pk)와 같은 역할. Post 인스턴스(레코드)의 author필드가 방문자와 동일한 경우에만 True.
      
      # 완전히 일치한다면, PostUpdate의 부모인 UpdateView에 dispatch()를 적용한 값을 response한다. -> GET일 경우 포스트를 작성할 수 있는 폼 페이지로 redirect 시켜준다.
      return super(PostUpdate, self).dispatch(request, *args, **kwargs)
    else:
      # import한 허가 거부 모듈을 response
      raise PermissionDenied


#FBV 방식
def new_comment(request, pk):
  # 비정상적인 방법으로 new_comment에 접근하는 시도를 방지하기 위해 로그인 안한 유저의 경우(else) PermissionDenied 발생시키기
  if request.user.is_authenticated:
    # pk값이 없을 경우 404
    post = get_object_or_404(Post, pk=pk)

    # submit 버튼 누른 후 POST 방식으로 전달되므로:
    if request.method == 'POST':
      # POST 방식으로 들어온 정보를 CommentForm의 형태로 가져오기
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
        # 유효성 검사가 통과되면 해당 내용으로 새 레코드를 만들어 저장.
        # commit=False로 잠시 저장하는 기능 미루기
        comment = comment_form.save(commit=False)
        # Comment 인스턴스만 가져와 post필드와 author필드 채우기
        comment.post = post
        comment.author = request.user
        # 둘다 채우고 나면 이제 저장하기
        comment.save()
        return redirect(comment.get_absolute_url())
    else:
      # 즉 GET방식일때 -> 브라우저 도메인창으로 직접 주소 입력해서 들어온 분은 pk=10인 페이지로 리다이렉트
      return redirect(post.get_absolute_url())
  else:
    raise PermissionDenied


# 댓글 수정 기능
# 로그인되지 않은 채로 CommentUpdate에 POST 방식으로 업데이트 하는 걸 막기 위해 LoginRequiredMixin
class CommentUpdate(LoginRequiredMixin, UpdateView):
  # Comment 모델 사용 선언
  model = Comment
  # form_class엔 models.py의 CommentForm
  form_class = CommentForm
  
  def dispatch(self, request, *args, **kwargs):
    # 댓글 수정 path에 접속하려는 사용자가 댓글 작성자와 다를 경우 PermissionDenied 제출
    if request.user.is_authenticated and request.user == self.get_object().author:
      return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
    else:
      raise PermissionDenied
    

# 댓글 삭제 메소드
def delete_comment(request, pk):
  # get_object_or_404 함수로 delete_comment에서 인자로 받은 pk값과 같은 pk 값을 가진 댓글을 쿼리셋으로 받아 comment 변수에 저장.
  comment = get_object_or_404(Comment, pk=pk)
  # 그 댓글이 달린 포스트를 post 변수에 저장. -> 댓 삭제된 후 그 댓글이 달려있던 페이지로 리다이렉트
  post = comment.post
  # 인증 확인
  if request.user.is_authenticated and request.user == comment.author:
    # 조건 만족시 댓글 삭제
    comment.delete()
    # 댓글 달렸던 페이지(아까 post에 comment.post 대입시켰음)의 경로로 리다이렉트
    return redirect(post.get_absolute_url())
  else:
    raise PermissionDenied