# Generated by Django 3.2 on 2023-04-20 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_costs', '0006_auto_20230420_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 20, 59, 7, 550221)),
        ),
        migrations.AlterField(
            model_name='flour',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 20, 59, 7, 550221)),
        ),
    ]
