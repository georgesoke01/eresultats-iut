# Generated by Django 5.1.4 on 2025-03-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_examconcours_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='examconcours',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
