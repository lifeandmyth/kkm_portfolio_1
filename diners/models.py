from django.db import models
import os
# 사용자 필드 구현을 위한 호출
from django.contrib.auth.models import User
# django-markdownx 호출 -> 마크다운 문법 적용하기
from markdownx.models import MarkdownxField
# 마크다운 문법으로 작성된 content 필드 값을 HTML로 변환하기 위해 필요한 기능 호출
from markdownx.utils import markdown


#Tag 모델 - Category 모델과 유사점이 많다. 
class Tag(models.Model):
  #unique=True : 명칭 중복 금지시키기
  name = models.CharField(max_length=50, unique=True)
  #SlugField는 '사람이 읽을 수 있는 텍스트'로 고유URL을 만들고 싶을 때 주로 사용.
  slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
  #allow_unicode로 한글도 입력 가능.

  def __str__(self):
    return self.name
  # category를 tag로 바꾼다.
  def get_absolute_url(self):
    return f'/diners/tag/{self.slug}/'
  # 복수형은 Tags로 멀쩡히 나오기에 삭제함.


#Category 모델 - 일부러 Post 클래스보다 앞에 배치해 category 변수가 값을 받을 수 있게끔 조정.
class Category(models.Model):
  #unique=True : 명칭 중복 금지시키기
  name = models.CharField(max_length=50, unique=True)
  #SlugField는 '사람이 읽을 수 있는 텍스트'로 고유URL을 만들고 싶을 때 주로 사용.
  slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
  #allow_unicode로 한글도 입력 가능.

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return f'/blog/category/{self.slug}/'
  
  class Meta:
    verbose_name_plural = 'Categories'

# Create your models here.
# 항상 models에 변동사항이 있을 경우 python manage.py makemigrations, python manage.py migrate 하는 것을 잊지 않도록.
class Post(models.Model):
  title = models.CharField(max_length=30)
  hook_text = models.CharField(max_length=100, blank=True)
  # content = models.TextField()
  # django-markdownx를 적용한다면:
  content = MarkdownxField()

  head_image = models.ImageField(upload_to='diners/images/%Y/%m/%d/', blank=True)
  file_upload = models.FileField(upload_to='diners/files/%Y/%m/%d/', blank=True)
  

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  #on_delete=models.CASCADE 
  #이 포스트의 작성자가 데이터베이스에서 삭제되었을 때 이 포스트도 같이 삭제된다는 의미.
  
  #이 경우 사용자가 삭제되어도 그 사용자가 작성한 글은 남겨두고 author 필드 값만 null로 바뀌도록 설정.
  #null=True를 추가함으로써 원래 null이 될 수 없는(정확히는 허용치 않는) 필드값이 null이 될 수 있게 한다.
  author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

  category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

  #Tags 필드는 Post와 다대다 관계이기 때문에 ForeignKey가 아닌 ManyToManyField를 사용.
  #연결된 태그가 삭제되면 해당 포스트의 tags필드는 알아서 빈 칸으로 바뀌기에 on_delete=models.SET_NULL은 설정 X.
  tags = models.ManyToManyField(Tag, null=True, blank=True)


  def __str__(self):
    return f"[{self.pk}]{self.title} :: {self.author}"
  
  def get_absolute_url(self):
    return f'/diners/{self.pk}/'
  
  def get_file_name(self):
    # 올린 파일의 명칭(경로 + 파일명)에서 파일명을 response
    return os.path.basename(self.file_upload.name)
  
  def get_file_ext(self):
    # 올린 파일의 파일명에서 확장자 부분만 response
    # .으로 요소를 나눈 리스트를 반환한 뒤, 그 중에서 [-1]번째 인덱스의 요소 (즉 확장자 부분)을 response
    return self.get_file_name().split('.')[-1]
  
  # 임포트한 markdown을 활용하는 메소드:
  # Post 레코드의 content 필드에 저장되어 있는 텍스트를 마크다운 문법을 적용해 HTML로 만든다:
  def get_content_markdown(self):
    return markdown(self.content)

  def get_avatar_url(self):
    if self.author.socialaccount_set.exists():
      return self.author.socialaccount_set.first().get_avatar_url()
    else:
      return f'https://doitdjango.com/avatar/id/1491/c4fc00950f0f17b8/svg/{{self.author.email}}'




# Comment 모델 만들기
# 댓글 기능을 만들려면, 어떤 포스트에 대한 댓글인지(post), 작성자는 누구고(author) 댓글 내용은 뭔지(content), 그리고 작성일시와 수정일시를 체크해 두는 것(created_at, modified_at)이 필요할 것이다.
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  # 처음 글 생성했을 때 시점 -> auto_now_add
  created_at = models.DateTimeField(auto_now_add=True)
  # 매번 수정할때마다 시점 -> auto_now
  modified_at = models.DateTimeField(auto_now=True)

  # 작성자명과 content내용을 출력하는 __str__ 함수:
  def __str__(self):
    return f'{self.author}::{self.content}'
  
  # 작성한 댓글을 빠르게 확인할 수 있도록 해당 댓글 위치로 바로 이동하는 VIEW ON SITE버튼
  #  #comment-{self.pk}: #이 HTML요소의 id를 의미함. 즉, 이와 같이 작성시 웹 브라우저가 해당 포스트의 페이지를 열고 comment-{self.pk}에 해당하는 위치로 이동한다는 것.
  def get_absolute_url(self):
    print('#comment-{self.pk}')
    return f'{self.post.get_absolute_url()}#comment-{self.pk}'
  
  # 아바타 설정하기
  def get_avatar_url(self):
    if self.author.socialaccount_set.exists():
      return self.author.socialaccount_set.first().get_avatar_url()
    else:
      # 그냥 흑백 아바타
      # return 'http://placehold.it/50x50'
      # 이거 대신 인물아바타 이미지로 현 아바타 함수에 응용: 접속한 방문자에 따라 아바타 이미지가 달라짐.(doitdjango.com/avatar/ 에서 지원)
      return f'https://doitdjango.com/avatar/id/1491/c4fc00950f0f17b8/svg/{self.author.email}'