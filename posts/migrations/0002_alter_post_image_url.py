# Generated by Django 4.2.16 on 2024-11-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.URLField(),
        ),
    ]
