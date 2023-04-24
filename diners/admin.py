from django.contrib import admin
# comment 기능 추가
from .models import Post, Category, Tag, Comment
# summernote 관련 라이브러리
from django_summernote.admin import SummernoteModelAdminMixin
# summernote_fields = ('content',)로 특정 부위에서만 쓰일 거면 굳이 '__all__'로 전부 호출할 필요 없음.

# django-markdownx를 적용하기
from markdownx.admin import MarkdownxModelAdmin


# Register your models here.
# only content field in Post model will have SummernoteWidget.
class PostAdmin(SummernoteModelAdminMixin):
    summernote_fields = ('content') # 구체적으로 Textfield에 적용한다는 의미(models.py에 확인)

# PostAdmin은 Summernote 때문에 추가.
# admin.site.register(Post, PostAdmin)
# 위의 코드에 Markdownx를 적용:
# admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Post, admin.ModelAdmin)
# 댓글 작성 및 수정, 삭제 항목 추가
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
class TagAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
