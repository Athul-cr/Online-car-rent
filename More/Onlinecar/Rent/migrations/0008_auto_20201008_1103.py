# Generated by Django 3.1 on 2020-10-08 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0007_auto_20201008_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Hi_km',
            field=models.IntegerField(default=0),
        ),
    ]