# Generated by Django 4.1.2 on 2022-11-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Result",
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
                ("task_id", models.CharField(max_length=50)),
                ("result", models.CharField(max_length=50)),
                ("status", models.CharField(max_length=50)),
                ("date_start", models.DateTimeField()),
                ("date_done", models.DateTimeField()),
            ],
        ),
    ]
