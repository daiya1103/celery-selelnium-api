# Generated by Django 4.2.3 on 2023-09-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scrape", "0012_common"),
    ]

    operations = [
        migrations.RemoveField(model_name="mercari", name="status",),
        migrations.AddField(
            model_name="mercari",
            name="on_sale",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="mercari",
            name="sold_out",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="mercari",
            name="order",
            field=models.CharField(default="すべて", max_length=255),
        ),
    ]
