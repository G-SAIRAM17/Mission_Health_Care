# Generated by Django 5.0.6 on 2024-07-20 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IntegratedHealthCare', '0004_alter_patientsignup_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='timeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('max_appointments', models.IntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IntegratedHealthCare.doctorsignup')),
            ],
        ),
    ]
