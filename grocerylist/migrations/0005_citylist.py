# Generated by Django 4.2.9 on 2024-04-21 00:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("grocerylist", "0004_alter_grocerylist_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="CityList",
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
                ("city", models.CharField(max_length=255)),
                ("state_id", models.CharField(max_length=10)),
                ("state_name", models.CharField(max_length=255)),
                ("county_name", models.CharField(max_length=255)),
                ("lat", models.FloatField()),
                ("lng", models.FloatField()),
                ("zips", models.CharField(max_length=1000)),
            ],
        ),
    ]