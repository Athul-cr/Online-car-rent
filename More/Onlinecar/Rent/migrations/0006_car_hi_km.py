# Generated by Django 3.1 on 2020-10-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0005_remove_car_hi_km'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='Hi_km',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
