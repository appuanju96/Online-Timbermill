# Generated by Django 2.2.7 on 2020-04-22 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_usell_umail'),
    ]

    operations = [
        migrations.CreateModel(
            name='timber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=100)),
            ],
        ),
    ]