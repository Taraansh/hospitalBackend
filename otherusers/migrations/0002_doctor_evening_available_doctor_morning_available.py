# Generated by Django 4.2 on 2023-05-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otherusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='evening_available',
            field=models.CharField(choices=[('available', 'Available'), ('not vailable', 'Not Available')], default='available', max_length=20),
        ),
        migrations.AddField(
            model_name='doctor',
            name='morning_available',
            field=models.CharField(choices=[('available', 'Available'), ('not vailable', 'Not Available')], default='available', max_length=20),
        ),
    ]
