# Generated by Django 5.1.4 on 2025-01-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='is_historical',
            field=models.BooleanField(default=True),
        ),
    ]
