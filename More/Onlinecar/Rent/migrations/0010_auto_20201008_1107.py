# Generated by Django 3.1 on 2020-10-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0009_auto_20201008_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='seat_Select',
            field=models.IntegerField(choices=[(1, '5'), (2, '7')]),
        ),
    ]