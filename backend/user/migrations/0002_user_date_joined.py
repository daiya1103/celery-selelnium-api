# Generated by Django 4.2.3 on 2023-12-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateField(default='2023-11-03'),
            preserve_default=False,
        ),
    ]
