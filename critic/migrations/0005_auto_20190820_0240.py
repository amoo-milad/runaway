# Generated by Django 2.2.3 on 2019-08-19 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('critic', '0004_auto_20190820_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateField(verbose_name='publish date'),
        ),
    ]