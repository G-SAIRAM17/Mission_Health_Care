# Generated by Django 5.0.7 on 2024-07-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IntegratedHealthCare', '0007_remove_labtechniciansignup_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=100)),
                ('hname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
