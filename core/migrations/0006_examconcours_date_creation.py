# Generated by Django 5.1.4 on 2025-03-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_examconcours_titre'),
    ]

    operations = [
        migrations.AddField(
            model_name='examconcours',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, default='2024-01-01 00:00:00'),
            preserve_default=False,
        ),
    ]
