# Generated by Django 2.2 on 2019-05-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pseudo_test', '0004_auto_20190506_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
