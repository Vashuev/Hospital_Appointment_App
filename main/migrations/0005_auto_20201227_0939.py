# Generated by Django 3.1.2 on 2020-12-27 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
