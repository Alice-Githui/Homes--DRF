# Generated by Django 3.2.4 on 2021-06-09 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourhomes', '0015_alter_home_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='location',
        ),
    ]
