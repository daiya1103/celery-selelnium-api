# Generated by Django 4.2.3 on 2023-11-16 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0021_alter_researchresult_seller_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchresult',
            name='condition',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researchresult',
            name='sell_status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
