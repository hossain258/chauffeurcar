# Generated by Django 4.2.1 on 2023-06-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_car", "0021_alter_review_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="content",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]