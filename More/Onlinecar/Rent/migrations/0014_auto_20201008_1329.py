# Generated by Django 3.1 on 2020-10-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0013_auto_20201008_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='Hi_km',
            field=models.CharField(default='check', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='lw_km',
            field=models.CharField(default='check tow', max_length=120),
            preserve_default=False,
        ),
    ]
