# Generated by Django 3.0.7 on 2020-09-11 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Train_app', '0005_ticketmodel_ticket_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketmodel',
            old_name='destination_time',
            new_name='Arrival',
        ),
        migrations.RenameField(
            model_name='ticketmodel',
            old_name='origin_time',
            new_name='Departure',
        ),
    ]
