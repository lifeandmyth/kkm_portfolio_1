from django.db import models

# Create your models here.

class Dashboard:
    def get_absolute_url(self):
        return f'/foodies_list/dashboard.html/'
    
# class SearchDiv(models.Model):
#     num = models.IntegerField()
    
    #SlugField는 '사람이 읽을 수 있는 텍스트'로 고유URL을 만들고 싶을 때 주로 사용.
    #allow_unicode로 한글도 입력 가능.
    # slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    
    # def get_absolute_url(self):
    #     return f'/foodies_list/dashboard/?foodies={self.num}/'
    
