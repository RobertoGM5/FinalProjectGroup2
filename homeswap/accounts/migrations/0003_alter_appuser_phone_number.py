# Generated by Django 5.0.4 on 2024-05-20 18:22

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_appuser_postal_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appuser",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region="DE"
            ),
        ),
    ]