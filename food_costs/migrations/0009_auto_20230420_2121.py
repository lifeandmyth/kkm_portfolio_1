# Generated by Django 3.2 on 2023-04-20 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_costs', '0008_auto_20230420_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 21, 21, 39, 866891)),
        ),
        migrations.AlterField(
            model_name='flour',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 21, 21, 39, 866891)),
        ),
        migrations.AlterField(
            model_name='sugar',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 21, 21, 39, 866891)),
        ),
    ]
