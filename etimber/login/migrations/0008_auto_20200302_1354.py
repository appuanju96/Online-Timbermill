# Generated by Django 2.2.7 on 2020-03-02 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20200302_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
