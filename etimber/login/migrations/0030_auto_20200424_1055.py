# Generated by Django 2.2.7 on 2020-04-24 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0029_remove_sell_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='mob',
            new_name='wood_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='stus',
        ),
    ]
