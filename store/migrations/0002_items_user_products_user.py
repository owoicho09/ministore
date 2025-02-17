# Generated by Django 5.0.6 on 2024-12-27 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
        ("userauth", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="items",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="userauth.user",
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="userauth.user",
            ),
        ),
    ]
