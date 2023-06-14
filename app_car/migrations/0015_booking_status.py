# Generated by Django 4.2.1 on 2023-06-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_car", "0014_alter_booking_is_return_journey_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("confirmed", "Confirmed"),
                    ("action_pending", "Action Pending"),
                    ("completed", "Completed"),
                    ("canceled", "Canceled"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
