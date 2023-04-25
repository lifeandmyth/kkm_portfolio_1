from django.db import models
from django.utils import timezone

# Create your models here.

class Eggs(models.Model): 
    #날짜는 non-nullable field 값이기 때문에, default설정이 필수다.
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "계란(/30개)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'
    

class Flour(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "밀가루(/kg)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'
    
class Sugar(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "설탕(/kg)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'
    
class Pepper(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "건고추(/0.6kg)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'

class SaltedMackerel(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "고등어_염장(/1마리)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'

class SaltedShrimp(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "새우젓(/1kg)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'

class Anchovy(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "건멸치(/0.1kg)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'

class Squid(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "물오징어(/1마리)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'
    
class Rice(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "쌀(/20kg)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'
    
class ChapRice(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "찹쌀(/1kg)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'
    
class WhiteBeans(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "흰콩(/1kg)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'
    
class RedBeans(models.Model): 
    date = models.DateTimeField(default=timezone.now())
    unit_price = models.IntegerField()
    name = "팥(/0.5kg)"
    def __str__(self):
        return f'{self.date}--{self.unit_price}'
    

class FlourFood(models.Model):
    date = models.DateTimeField(default=timezone.now())
    meal_price = models.IntegerField()
    name = "자장면(/1인분)"
    def __str__(self):
        return f'{self.date}--{self.meal_price}'


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
