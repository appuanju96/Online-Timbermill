# Generated by Django 2.2.7 on 2020-05-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0066_delete_premium'),
    ]

    operations = [
        migrations.CreateModel(
            name='membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('cvv', models.IntegerField()),
            ],
        ),
    ]
