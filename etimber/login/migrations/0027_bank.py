# Generated by Django 2.2.7 on 2020-04-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0026_timber'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.FloatField()),
            ],
        ),
    ]