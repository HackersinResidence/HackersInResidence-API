# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HIR', '0011_auto_20160714_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
