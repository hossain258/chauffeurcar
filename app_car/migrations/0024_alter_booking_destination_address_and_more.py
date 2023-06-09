# Generated by Django 4.2.1 on 2023-06-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_car", "0023_alter_review_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="destination_address",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="journey_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="journey_time",
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="pickup_address",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="privacy_agree",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="terms_agree",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="review",
            name="email",
            field=models.EmailField(max_length=155, null=True),
        ),
    ]
