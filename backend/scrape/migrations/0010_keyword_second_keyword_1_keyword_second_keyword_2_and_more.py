# Generated by Django 4.2.3 on 2023-09-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scrape", "0009_keyword_keyword"),
    ]

    operations = [
        migrations.AddField(
            model_name="keyword",
            name="second_keyword_1",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="keyword",
            name="second_keyword_2",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="keyword",
            name="second_keyword_3",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="keyword",
            name="second_keyword_4",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="keyword",
            name="second_keyword_5",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.DeleteModel(name="SecondKeyword",),
    ]