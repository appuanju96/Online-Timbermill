# Generated by Django 2.2.7 on 2020-03-25 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='mname',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='uname',
        ),
    ]
