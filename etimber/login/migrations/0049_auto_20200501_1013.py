# Generated by Django 2.2.7 on 2020-05-01 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0048_auto_20200430_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stvisit',
            name='cir',
        ),
        migrations.RemoveField(
            model_name='stvisit',
            name='lenn',
        ),
        migrations.RemoveField(
            model_name='stvisit',
            name='mill_name',
        ),
        migrations.RemoveField(
            model_name='stvisit',
            name='mname',
        ),
        migrations.RemoveField(
            model_name='stvisit',
            name='rat',
        ),
        migrations.RemoveField(
            model_name='stvisit',
            name='type_wd',
        ),
        migrations.RemoveField(
            model_name='stvisit',
            name='user',
        ),
        migrations.RemoveField(
            model_name='stvisit',
            name='usname',
        ),
        migrations.RemoveField(
            model_name='stvisit',
            name='wid',
        ),
    ]
