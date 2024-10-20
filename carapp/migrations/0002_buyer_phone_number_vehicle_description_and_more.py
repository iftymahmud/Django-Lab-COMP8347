# Generated by Django 4.2.16 on 2024-10-05 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("carapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="buyer",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="buyer",
            name="area",
            field=models.CharField(
                choices=[
                    ("C", "Chatham"),
                    ("W", "Windsor"),
                    ("LS", "LaSalle"),
                    ("A", "Amherstburg"),
                    ("L", "Lakeshore"),
                    ("LE", "Leamington"),
                ],
                default="C",
                max_length=2,
            ),
        ),
        migrations.CreateModel(
            name="OrderVehicle",
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
                ("quantity", models.PositiveIntegerField()),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Cancelled"),
                            (1, "Placed"),
                            (2, "Shipped"),
                            (3, "Delivered"),
                        ],
                        default=1,
                    ),
                ),
                ("last_updated", models.DateField(auto_now=True)),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="carapp.buyer"
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="carapp.vehicle"
                    ),
                ),
            ],
        ),
    ]
