# Generated by Django 3.2 on 2022-05-26 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crud',
            name='vitsi',
        ),
    ]
