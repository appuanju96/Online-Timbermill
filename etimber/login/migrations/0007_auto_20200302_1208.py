# Generated by Django 2.2.7 on 2020-03-02 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_mill_uname'),
    ]

    operations = [
        migrations.CreateModel(
            name='sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_wood', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='usell',
        ),
    ]