# Generated by Django 2.2.7 on 2020-03-26 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_auto_20200326_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='mob',
        ),
    ]
