# Generated by Django 2.0 on 2017-12-29 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitalian', '0011_auto_20171228_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='progress',
        ),
    ]