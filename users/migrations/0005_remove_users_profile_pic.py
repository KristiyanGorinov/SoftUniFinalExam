# Generated by Django 4.2.16 on 2024-11-17 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_users_profile_pic_alter_users_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='profile_pic',
        ),
    ]
