# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pharma', '0004_auto_20171101_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='cust_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='qty',
            field=models.IntegerField(),
        ),
    ]
