# Generated by Django 2.2.7 on 2020-04-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0031_auto_20200424_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='user',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
