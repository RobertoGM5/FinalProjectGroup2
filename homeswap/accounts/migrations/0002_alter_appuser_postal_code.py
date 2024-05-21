# Generated by Django 5.0.4 on 2024-05-21 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(999999)]),
        ),
    ]
