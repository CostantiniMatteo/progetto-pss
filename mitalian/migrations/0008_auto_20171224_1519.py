# Generated by Django 2.0 on 2017-12-24 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitalian', '0007_collection_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='last_feched',
            new_name='last_fetched',
        ),
    ]