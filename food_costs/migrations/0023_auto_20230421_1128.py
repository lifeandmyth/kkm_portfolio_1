# Generated by Django 3.2 on 2023-04-21 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_costs', '0022_auto_20230421_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 11, 28, 28, 631885)),
        ),
        migrations.AlterField(
            model_name='flour',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 11, 28, 28, 631885)),
        ),
        migrations.AlterField(
            model_name='sugar',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 11, 28, 28, 631885)),
        ),
    ]
