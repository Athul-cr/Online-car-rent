# Generated by Django 3.1 on 2020-10-08 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0010_auto_20201008_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Hi_km',
            field=models.IntegerField(),
        ),
    ]
