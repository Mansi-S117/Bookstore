# Generated by Django 5.1.1 on 2024-10-24 08:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_alter_dailysalesreport_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="seller",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="seller",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sales",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
