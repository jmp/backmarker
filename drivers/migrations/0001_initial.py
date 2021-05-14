# Generated by Django 3.2.2 on 2021-05-14 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Driver",
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
                ("number", models.IntegerField(null=True)),
                ("code", models.CharField(max_length=3, null=True)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("nationality", models.CharField(max_length=255)),
                ("wiki_url", models.URLField(db_column="url", unique=True)),
            ],
        ),
    ]