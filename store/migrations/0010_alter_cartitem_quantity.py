# Generated by Django 4.1.7 on 2023-04-29 07:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0009_alter_cart_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]
