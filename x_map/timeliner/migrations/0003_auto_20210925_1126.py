# Generated by Django 3.2.7 on 2021-09-25 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeliner', '0002_auto_20210925_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.RemoveField(
            model_name='location',
            name='country',
        ),
        migrations.RemoveField(
            model_name='location',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='location',
            name='road',
        ),
        migrations.RemoveField(
            model_name='location',
            name='state',
        ),
    ]
