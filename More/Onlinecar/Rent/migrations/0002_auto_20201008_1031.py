# Generated by Django 3.1 on 2020-10-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='Hi_km',
            field=models.IntegerField(default='select'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='location',
            field=models.CharField(default='select', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='lw_km',
            field=models.IntegerField(default='200'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='price_high',
            field=models.IntegerField(default='200'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='seat_Select',
            field=models.IntegerField(choices=[('5', '5'), ('7', '7')], default='5'),
            preserve_default=False,
        ),
    ]
