# Generated by Django 3.2.4 on 2021-06-09 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourhomes', '0009_alter_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_profile',
            new_name='is_user',
        ),
    ]
