# Generated by Django 4.2.1 on 2023-06-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_car", "0002_services_alter_contact_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=100)),
                ("mobile", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=100)),
                ("payment_type", models.IntegerField(default=0)),
                ("journey_date", models.DateField()),
                ("journey_time", models.DateField()),
                ("passenger_number", models.IntegerField(default=0)),
                ("flight_number", models.IntegerField(default=0)),
                ("main_luggage", models.IntegerField(default=0)),
                ("hand_luggage", models.IntegerField(default=0)),
                ("pickup_address", models.CharField(max_length=200)),
                ("destination_address", models.CharField(max_length=200)),
                ("is_return_journey", models.BooleanField(default=False)),
                ("return_journey_date", models.DateField()),
                ("return_journey_time", models.DateField()),
                ("return_passenger_number", models.IntegerField(default=0)),
                ("return_flight_number", models.IntegerField(default=0)),
                ("return_main_luggage", models.IntegerField(default=0)),
                ("return_hand_luggage", models.IntegerField(default=0)),
                ("return_pickup_address", models.CharField(max_length=200)),
                ("return_destination_address", models.CharField(max_length=200)),
                ("booking_note", models.TextField(max_length=1000)),
                ("service_type", models.IntegerField(default=0)),
                ("promo_code", models.CharField(blank=True, max_length=20, null=True)),
                ("privacy_agree", models.BooleanField(default=False)),
                ("terms_agree", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ("-created_at",),
                "abstract": False,
            },
        ),
    ]
