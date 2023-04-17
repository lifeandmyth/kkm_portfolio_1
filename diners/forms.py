from django import forms
from .models import Post

#CommentForm 구현하기
from .models import Comment


from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category', ]
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px', 'font': 'gothic'}}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 튜플이므로 , 추가
        fields = ('content',)