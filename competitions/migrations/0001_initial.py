# Generated by Django 4.2.16 on 2024-12-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubs', '0002_alter_club_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('context', models.TextField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='clubs.club')),
            ],
        ),
    ]
