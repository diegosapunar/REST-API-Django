# Generated by Django 3.0.5 on 2020-05-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herokuapp', '0002_auto_20200501_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='imagen',
            field=models.CharField(max_length=400),
        ),
    ]
