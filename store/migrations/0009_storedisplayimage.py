# Generated by Django 5.0.6 on 2025-01-13 09:35

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0008_items_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="StoreDisplayImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "image",
                    cloudinary.models.CloudinaryField(
                        blank=True, max_length=255, null=True, verbose_name="image"
                    ),
                ),
            ],
        ),
    ]
