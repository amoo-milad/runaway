# Generated by Django 2.2.3 on 2019-08-20 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('critic', '0010_auto_20190821_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='genre_name',
        ),
    ]
