# Generated by Django 4.2 on 2023-05-07 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_alter_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
    ]
