# Generated by Django 2.2.3 on 2019-11-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('critic', '0017_manual_migration_for_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(max_length=2000),
        ),
    ]
