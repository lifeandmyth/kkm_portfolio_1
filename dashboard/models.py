from django.db import models

# Create your models here.

class Dashboard:
  def get_absolute_url(self):
    return f'/dashboard/dashboard.html/'