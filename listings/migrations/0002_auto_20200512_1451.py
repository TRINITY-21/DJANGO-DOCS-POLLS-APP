# Generated by Django 3.0.6 on 2020-05-12 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='is_published',
            field=models.BooleanField(default='True'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
