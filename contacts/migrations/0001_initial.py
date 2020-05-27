# Generated by Django 3.0.6 on 2020-05-16 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('message', models.TextField(blank=True)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
