# Generated by Django 3.1 on 2020-10-08 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=120)),
                ('Modd', models.CharField(max_length=120)),
                ('seat_Select', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('lw_km', models.CharField(max_length=120)),
                ('Hi_km', models.CharField(max_length=120)),
                ('price_high', models.CharField(max_length=120)),
                ('price', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='images')),
                ('brand_nme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rent.brand')),
            ],
        ),
    ]
