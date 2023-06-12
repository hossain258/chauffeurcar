# Generated by Django 4.2.1 on 2023-06-11 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_car", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Services",
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
                ("title", models.CharField(blank=True, max_length=120, null=True)),
                ("headline", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "service_img",
                    models.ImageField(blank=True, null=True, upload_to="services"),
                ),
            ],
            options={
                "verbose_name_plural": "Courses",
            },
        ),
        migrations.AlterModelOptions(
            name="contact",
            options={"ordering": ("-created_at",)},
        ),
        migrations.RenameField(
            model_name="contact",
            old_name="date_created",
            new_name="created_at",
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(blank=True, max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.TextField(blank=True, max_length=1200, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
