# Generated by Django 2.2.7 on 2020-03-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20200326_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='uname',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
