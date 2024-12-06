# Generated by Django 5.1.4 on 2024-12-05 06:05

import tasks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='token',
            field=models.CharField(default=tasks.models.generate_unique_token, max_length=64, unique=True),
        ),
    ]
