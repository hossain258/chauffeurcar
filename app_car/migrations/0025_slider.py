# Generated by Django 4.2.1 on 2023-06-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_car", "0024_alter_booking_destination_address_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Slider",
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
                (
                    "slider_image",
                    models.ImageField(blank=True, null=True, upload_to="slider"),
                ),
                (
                    "slider_title",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "slider_text",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
            ],
        ),
    ]
