# Generated by Django 2.2.7 on 2020-05-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0052_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='stvisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stime', models.TextField()),
            ],
        ),
    ]
