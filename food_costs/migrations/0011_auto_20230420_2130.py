# Generated by Django 3.2 on 2023-04-20 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_costs', '0010_auto_20230420_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 21, 30, 1, 450376)),
        ),
        migrations.AlterField(
            model_name='flour',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 21, 30, 1, 450376)),
        ),
        migrations.AlterField(
            model_name='sugar',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 21, 30, 1, 450376)),
        ),
    ]
