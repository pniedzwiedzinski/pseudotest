# Generated by Django 2.2 on 2019-04-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pseudo_test', '0002_auto_20190430_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score_date',
            field=models.DateTimeField(),
        ),
    ]
