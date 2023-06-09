# Generated by Django 4.1.6 on 2023-06-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_car', '0005_services_is_featured_services_thumbnail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_note',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='destination_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='is_return_journey',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pickup_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_destination_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_journey_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_journey_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_pickup_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
