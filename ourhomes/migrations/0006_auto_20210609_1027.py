# Generated by Django 3.2.4 on 2021-06-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourhomes', '0005_auto_20210609_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]
