# Generated by Django 4.1.6 on 2023-06-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_car', '0011_alter_booking_journey_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='flight_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_flight_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
