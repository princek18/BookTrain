# Generated by Django 3.0.7 on 2020-09-11 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Train_app', '0003_ticketmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='passengermodel',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passengers', to='Train_app.TicketModel'),
        ),
    ]