# Generated by Django 4.2.9 on 2024-04-21 03:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("grocerylist", "0008_rename_rating_grocerylist_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="storelist",
            name="imagelink",
            field=models.URLField(null=True),
        ),
    ]