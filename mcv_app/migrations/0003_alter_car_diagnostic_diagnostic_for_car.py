# Generated by Django 4.1.6 on 2023-04-27 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mcv_app", "0002_alter_driver_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car_diagnostic",
            name="diagnostic_for_car",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="mcv_app.car"
            ),
        ),
    ]
