# Generated by Django 3.2.4 on 2021-06-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourhomes', '0013_alter_user_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='image',
        ),
        migrations.AddField(
            model_name='home',
            name='images',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
