# Generated by Django 4.2.16 on 2024-11-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_users_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
