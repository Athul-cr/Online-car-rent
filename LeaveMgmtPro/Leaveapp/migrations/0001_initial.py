# Generated by Django 3.1 on 2020-10-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leavemgmnt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AplyDate', models.DateField()),
                ('toDate', models.DateField()),
                ('Reason', models.CharField(max_length=120)),
                ('days', models.CharField(max_length=120)),
                ('leave_status', models.CharField(choices=[('pending', 'pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('None', 'None')], default='None', max_length=120)),
                ('Total_leave', models.IntegerField(default=0)),
            ],
        ),
    ]
