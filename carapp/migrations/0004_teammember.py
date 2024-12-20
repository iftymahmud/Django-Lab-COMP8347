# Generated by Django 4.2.16 on 2024-10-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carapp", "0003_alter_vehicle_car_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeamMember",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("semester", models.IntegerField()),
                ("personal_link", models.URLField()),
            ],
            options={
                "ordering": ["first_name"],
            },
        ),
    ]
