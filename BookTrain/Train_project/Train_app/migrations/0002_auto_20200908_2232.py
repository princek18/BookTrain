# Generated by Django 3.0.7 on 2020-09-08 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Train_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passengermodel',
            old_name='p_age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='passengermodel',
            old_name='p_berth',
            new_name='Berth',
        ),
        migrations.RenameField(
            model_name='passengermodel',
            old_name='p_gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='passengermodel',
            old_name='p_name',
            new_name='Passenger_name',
        ),
    ]
