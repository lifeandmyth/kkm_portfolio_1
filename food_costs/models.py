from django.db import models
from django.utils import timezone

# Create your models here.

class Eggs(models.Model): 
    #날짜는 non-nullable field 값이기 때문에, default설정이 필수다.
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "계란"
    

class Flour(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "밀가루"
    
class Sugar(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "설탕"

#식량작물
# class Rice(models.Model): 
#     date = models.DateTimeField(default=timezone.now())
#     unit_price = models.IntegerField()
#     def __str__(self):
#         return f'{self.date}--{self.unit_price}'
# class ChapRice(models.Model): 
#     date = models.DateTimeField(default=timezone.now())
#     unit_price = models.IntegerField()
#     def __str__(self):
#         return f'{self.date}--{self.unit_price}'
# class WhiteBeans(models.Model): 
#     date = models.DateTimeField(default=timezone.now())
#     unit_price = models.IntegerField()
#     def __str__(self):
#         return f'{self.date}--{self.unit_price}'
# class RedBeans(models.Model): 
#     date = models.DateTimeField(default=timezone.now())
#     unit_price = models.IntegerField()
#     def __str__(self):
#         return f'{self.date}--{self.unit_price}'
