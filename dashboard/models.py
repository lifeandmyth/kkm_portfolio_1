from django.db import models
from django.utils import timezone


# Create your models here.
class FoodIngData(models.Model):
  #날짜는 non-nullable field 값이기 때문에, default설정이 필수다.
  date = models.DateTimeField(default=timezone.now())
  unit_price = models.IntegerField()
