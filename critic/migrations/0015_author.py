# Generated by Django 2.2.3 on 2019-09-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('critic', '0014_auto_20190925_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]