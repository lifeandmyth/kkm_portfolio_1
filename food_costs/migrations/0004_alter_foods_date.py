# Generated by Django 3.2 on 2023-04-20 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_costs', '0003_alter_foods_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 13, 16, 23, 73164)),
        ),
    ]