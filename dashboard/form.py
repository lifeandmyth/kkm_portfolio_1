from django.forms import ModelForm
from .models import FoodIngData

class FoodIngDataForm(ModelForm):
  class Meta:
    model = FoodIngData
    fields = '__all__'

