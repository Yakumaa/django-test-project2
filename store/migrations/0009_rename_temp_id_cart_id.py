# Generated by Django 4.1.7 on 2023-04-26 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_remove_cart_id_alter_cart_temp_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="temp_id",
            new_name="id",
        ),
    ]
