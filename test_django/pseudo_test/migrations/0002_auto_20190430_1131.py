# Generated by Django 2.2 on 2019-04-30 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pseudo_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='score',
            name='score_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 30, 11, 31, 15, 486160)),
        ),
    ]