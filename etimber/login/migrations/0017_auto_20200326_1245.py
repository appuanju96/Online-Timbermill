# Generated by Django 2.2.7 on 2020-03-26 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_booking_mname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='mname',
            new_name='mill_name',
        ),
    ]
