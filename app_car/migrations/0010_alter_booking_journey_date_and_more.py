# Generated by Django 4.1.6 on 2023-06-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_car', '0009_alter_booking_journey_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='journey_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='journey_time',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_journey_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_journey_time',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
