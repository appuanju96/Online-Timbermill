# Generated by Django 2.2.7 on 2020-04-25 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0032_sell_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='usname',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
