# Generated by Django 2.2.3 on 2019-09-25 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('critic', '0013_auto_20190821_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='author',
            new_name='author_name',
        ),
    ]
