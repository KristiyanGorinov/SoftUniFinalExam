# Generated by Django 4.2.16 on 2024-11-21 18:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_remove_users_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('image_url', models.URLField(help_text='Share your funniest furry photo URL')),
                ('content', models.TextField()),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='users.users')),
            ],
            options={
                'verbose_name': 'Post',
            },
        ),
    ]
