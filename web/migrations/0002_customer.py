# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=20)),
                ('customer_phone', models.CharField(max_length=11)),
                ('customer_addr', models.TextField()),
            ],
        ),
    ]
