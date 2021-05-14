# Generated by Django 3.2.2 on 2021-05-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Constructor",
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
                ("reference", models.CharField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("nationality", models.CharField(max_length=255)),
                ("wiki_url", models.URLField(db_column="url")),
            ],
        ),
    ]
