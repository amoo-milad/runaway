# Generated by Django 2.2.3 on 2019-08-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('critic', '0002_auto_20190726_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='publish date')),
                ('author', models.CharField(max_length=30)),
                ('movie', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]