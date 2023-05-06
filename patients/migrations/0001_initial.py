# Generated by Django 4.2 on 2023-04-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_first_name', models.CharField(max_length=50)),
                ('patient_last_name', models.CharField(max_length=50)),
                ('patient_dob', models.DateField()),
                ('patient_age', models.IntegerField()),
                ('patient_gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('patient_contact', models.CharField(max_length=10)),
                ('patient_email', models.CharField(max_length=50)),
                ('patient_address', models.CharField(max_length=50)),
                ('patient_password', models.CharField(default=123456789, max_length=50)),
            ],
        ),
    ]
