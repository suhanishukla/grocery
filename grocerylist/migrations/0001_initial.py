# Generated by Django 4.2.7 on 2024-02-03 20:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GroceryList",
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
                ("type", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("price", models.CharField(max_length=255)),
                ("rating", models.CharField(max_length=255)),
                ("inlist", models.BooleanField(default=True)),
            ],
        ),
    ]
