# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-17 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True),
        ),
    ]
