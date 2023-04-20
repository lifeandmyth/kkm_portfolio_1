from django.db import models
from django.utils import timezone
from food_costs.models import Eggs, Flour, Sugar


# Create your models here.
class EggsD(models.Model):
  date = Eggs().date
  unit_price = Eggs().unit_price
  name = "계란"
  def __str__(self):
    return f'{self.date}--{self.unit_price}'

class FlourD(models.Model):
  date = Flour().date
  unit_price = Flour().unit_price
  name = "밀가루"
  def __str__(self):
    return f'{self.date}--{self.unit_price}'
  
class Sugar(models.Model):
  date = Sugar().date
  unit_price = Sugar().unit_price
  name = "설탕"
  def __str__(self):
    return f'{self.date}--{self.unit_price}'
