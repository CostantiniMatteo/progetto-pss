# Generated by Django 2.0 on 2017-12-20 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitalian', '0001_initial'),
    ]

    operations = [
        migrations.RenameField('Collection', 'password_hash', 'password'),
    ]
